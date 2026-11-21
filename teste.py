# arquivo para testes unitarios manualmente
import json

def extencion(language):
    with open("model/languages.json", "r", encoding="utf-8") as file:
        datas = json.load(file)
    languages = list(datas)[int(language)]
    languages = datas[languages]
    return languages

extencion("0")