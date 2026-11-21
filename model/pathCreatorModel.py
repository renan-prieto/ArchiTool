import os

class PathCreatorModel:
    def __init__(self):
        self.path = ""
        # self.mvc = ['models', 'views', 'controllers']

    def create_path(self):
        '''
        Cria um diretorio
        '''
        os.mkdir(self.path)

    def validate_path(self):
        '''
        Valida um diretorio
        '''
        if not os.path.exists(self.path):
            return False
        return True

    def create_archive(self, name, path):
        '''
        Cria um arquivo
        '''
        archive = open(f"{path}/{name}", "w")
        archive.close()

    