class FrameworkPresenter:
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.lan_frame, self.languages = self.model.languages_frameworks()

    def choose_languages(self):
        lang = self.view.language(self.languages)
        extencion = self.model.extencion(lang)
        # LEMBRAR DE VER SE ESTÁ CHAMANDO A FUNÇAO DUAS VEZES

        return self.languages[int(lang)], extencion

    def choose_frameworks(self, lang):
        frame = self.view.select_framework(self.lan_frame[lang])
        return self.model.languages_frameworks()

    # LEMBRAR DE VER SE ESTÁ CHAMANDO A FUNÇAO DUAS VEZES
