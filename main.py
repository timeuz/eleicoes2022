from flask import Flask, render_template, url_for
import requests
import json

app = Flask(__name__, static_url_path='/projects/eleicoes2022/static')

@app.route('/')

def votosPresi():
    data = requests.get(
        'https://resultados.tse.jus.br/oficial/ele2022/545/dados-simplificados/br/br-c0001-e000545-r.json'
        )
    json_data = json.loads(data.content)

    candidato = []
    partido = []
    votos = []
    porcentagem = []

    for info in json_data['cand']:
        if info['seq'] == '1' or info['seq'] == '2':
            frmt_prcnt = info['pvap']+"%"
            frmt_votos = format(int(info['vap']), "1,d").replace(',','.')
            candidato.append(info['nm'])
            partido.append(info['cc'])
            votos.append(frmt_votos)
            porcentagem.append(frmt_prcnt)
    return render_template("index.html",
                          len_cand = len(candidato),
                          candidato = candidato,
                          len_vot = len(votos),
                          votos = votos,
                          len_porc = len(porcentagem),
                          porcentagem = porcentagem
                          )

if __name__ == '__main__':
   app.run()