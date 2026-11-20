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

    
    