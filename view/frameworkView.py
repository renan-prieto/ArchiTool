class FrameworkView:
    def language(self, languages):
        for lan in range(len(languages)):
            print(f"{lan}. {languages[lan]}")
        return input("Escolha sua Linguagem: ")
        
    def select_framework(self, frameworks):
        count = 0
        for f in frameworks:
            count += 1
            print(f"{count}. {f}")
        print("0. Sem Framework")
        return input("Escolha: ")