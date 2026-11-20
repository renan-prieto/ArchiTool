class PathCreatorView:
    def menu_inicial(self):
        print("Criar Arquitetura")
        print("1. MVC")
        print("2. MVP")
        print("3. MVVM")
        print("4. MVVM-C")
        print("5. VIPER")
        return input("Escolha uma opcao: ")
    
    def extensao(self):
        return input("Escolha a linguagem: ")

    def repositorio(self):
        return input("Nome do projeto: ")
        
    def mensagem(self, mensagem):
        print("\n", mensagem)