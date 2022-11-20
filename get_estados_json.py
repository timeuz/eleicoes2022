from flask import Flask, render_template, url_for
import requests
import json

urna = "545"
estados = ("AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PR", "PB", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO")
votosest = {'ac':{},'al':{},'ap':{},'am':{},'ba':{},'ce':{},'df':{},'es':{},'go':{},'ma':{},'mt':{},'ms':{},'mg':{},'pa':{},'pr':{},'pb':{},'pe':{},'pi':{},'rj':{},'rn':{},'rs':{},'ro':{},'rr':{},'sc':{},'sp':{},'se':{},'to':{}}
estados = ("AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PR", "PB", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO")

for estado in estados:
        estado = estado.lower()
        dataest = requests.get(
            "https://resultados.tse.jus.br/oficial/ele2022/" + urna + "/dados-simplificados/" + estado + "/" + estado + "-c0001-e000" + urna + "-r.json"
            )
        json_dataest = json.loads(dataest.content)
        json_file = json.dumps(json_dataest)
        with open('static/'+estado+'.json','w') as dwnld:
            dwnld.write(json_file)
