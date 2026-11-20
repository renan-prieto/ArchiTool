class FrameworkView:
    def language(self, languages):
        for lan in range(len(languages)):
            print(f"{lan}. {languages[lan]}")
        return input("Escolha sua Linguagem: ")
        
    def framework(self, language, frameworks):
        count = 0
        for f in frameworks[language]:
            count += 1
            print(f"{count}. {f}")
        print("0. Sem Framework")
        return input("Escolha: ")