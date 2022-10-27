from flask import Flask, render_template, url_for
import requests
import json

app = Flask(__name__, static_url_path='/projects/eleicoes2022/static')

@app.route('/')

def votosPresi():
    urna = "545"
    estados = ("AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PR", "PB", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO")
    votosest = {'ac':{},'al':{},'ap':{},'am':{},'ba':{},'ce':{},'df':{},'es':{},'go':{},'ma':{},'mt':{},'ms':{},'mg':{},'pa':{},'pr':{},'pb':{},'pe':{},'pi':{},'rj':{},'rn':{},'rs':{},'ro':{},'rr':{},'sc':{},'sp':{},'se':{},'to':{}}
    aux = 0
    databr = requests.get(
        'https://resultados.tse.jus.br/oficial/ele2022/'+urna+'/dados-simplificados/br/br-c0001-e000'+urna+'-r.json'
        )

    json_databr = json.loads(databr.content)

    candidato = []
    partido = []
    votos = []
    porcentagem = []
    vbrancos = format(int(json_databr['vb']), "1,d").replace(',','.')
    pvbrancos = json_databr['pvb']+"%"
    vnulos = format(int(json_databr['tvn']), "1,d").replace(',','.')
    pvnulos = json_databr['ptvn']+"%"
    comp = format(int(json_databr['c']), "1,d").replace(',','.')
    pcomp = json_databr['pc']+"%"
    abst = format(int(json_databr['a']), "1,d").replace(',','.')
    pabst = json_databr['pa']+"%"

    for info in json_databr['cand']:
        if info['seq'] == '1' or info['seq'] == '2':
            frmt_prcnt = info['pvap']+"%"
            frmt_votos = format(int(info['vap']), "1,d").replace(',','.')
            candidato.append(info['nm'])
            partido.append(info['cc'])
            votos.append(frmt_votos)
            porcentagem.append(frmt_prcnt)
    
    for estado in estados:
        estado = estado.lower()
        dataest = requests.get(
            "https://resultados.tse.jus.br/oficial/ele2022/" + urna + "/dados-simplificados/" + estado + "/" + estado + "-c0001-e000" + urna + "-r.json"
            )
        json_dataest = json.loads(dataest.content)
        for i in json_dataest:
            if json_dataest['cand'][0]['n'] == '13':
                votosest[estado]['13'] = json_dataest['cand'][0]['pvap']
                votosest[estado]['22'] = json_dataest['cand'][1]['pvap']
            elif json_dataest['cand'][0]['n'] == '22':
                votosest[estado]['22'] = json_dataest['cand'][0]['pvap']
                votosest[estado]['13'] = json_dataest['cand'][1]['pvap']
            else:
                continue
    print(votosest)
    return render_template("index.html",
                          len_cand = len(candidato),
                          candidato = candidato,
                          len_vot = len(votos),
                          votos = votos,
                          len_porc = len(porcentagem),
                          porcentagem = porcentagem,
                          vbrancos = vbrancos,
                          pvbrancos = pvbrancos,
                          vnulos = vnulos,
                          pvnulos = pvnulos,
                          comp = comp,
                          pcomp = pcomp,
                          abst = abst,
                          pabst = pabst,
                          estados = estados,
                          votosest = votosest,
                          aux = aux
                          )

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8080)