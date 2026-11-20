import os

class PathCreatorModel:
    def __init__(self):
        self.path = ""
        # self.mvc = ['models', 'views', 'controllers']

    def create_path(self):
        os.mkdir(self.path)

    def validate_path(self):
        if not os.path.exists(self.path):
            return False
        return True

    def create_archive(self, name, path):
        archive = open(f"{path}/{name}", "w")
        archive.close()

    