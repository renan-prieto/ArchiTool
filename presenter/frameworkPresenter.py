class FrameworkPresenter:
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.lan_frame, self.languages = self.model.languages_frameworks()

    def choose_languages(self):
        lang = self.view.language(self.languages)
        return self.languages[int(lang)]

    def choose_frameworks(self, lang):
        frame = self.view.select_framework(self.lan_frame[lang])
        return self.lan_frame[lang][int(frame)]

    def handle_choices(self):
        language = self.choose_languages()
        framework = self.choose_frameworks(language)
        