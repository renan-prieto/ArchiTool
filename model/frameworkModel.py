import os
import json

class FrameworkModel:
    def languages_frameworks(self):
        linguages = []
        lang_frame = {}

        with open("model/commands.json", "r", encoding="utf-8") as file:
            datas = json.load(file)

        for lang, lista in datas.items():
            lang_frame.update([(lang, list(lista.keys()))])
            linguages.append(lang)
        
        return lang_frame, linguages

    def extencion(self, language):
        '''
        Retorna a extenção da linguagem selecionada
        Ex: linguagem-> Python, retorno->py
        '''
        with open("model/languages.json", "r", encoding="utf-8") as file:
            datas = json.load(file)

        print("language ",language)

        x = list(datas)
        print("language ",language)
        print("x ", x)
        
        y = x[int(language)]
        print("y ", y)
        return datas[y]

    def framework(self, frame):
        '''
        retornar o framework na qual foi escolhido
        '''
        with open("model/languages.json", "r", encoding="utf-8") as file:
            datas = json.load(file)
        