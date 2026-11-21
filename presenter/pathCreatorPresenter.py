class PathCreatorPresenter:
    def __init__(self, view, model):
        self.view = view
        self.model = model
        self.arch = []
        
    def create_arch(self, opcao, extensao, repositorio):
        try:
            if opcao == "1":   #MVC
                self.arch = ["models", "views", "controllers"]
            elif opcao == "2": #MVP
                self.arch = ["models", "views", "presenters"]
            elif opcao == "3": #MVVM
                self.arch = ["models", "views", "viewmodels"]
            elif opcao == "4": #MVVM-C
                self.arch = ["models", "views", "viewmodels", "coordinators"]
            elif opcao == "5": #VIPER
                self.arch = ["views", "interactors", "presenters", "entitys", "routers"]
                
            else:
                self.view.mensagem("Opcao invalida")
                return

            self.model.path = repositorio
            self.model.create_path()

            for path in self.arch:
                self.model.path = f"{repositorio}/{path}"
                self.model.create_path()
                self.model.create_archive(f"example{path[0:-1].capitalize()}.{extensao}", f"./{repositorio}/{path}")

                if not self.model.validate_path():
                    self.model.create_path()
                    self.view.mensagem(f"Arquitetura {self.model.path} criada com sucesso!")
                else:
                    self.view.mensagem(f"Arquitetura {self.model.path} ja existe!")
            
            

        except Exception as e:
            self.view.mensagem(f"Erro ao criar a arquitetura: {str(e)}")