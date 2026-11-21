from model.pathCreatorModel import PathCreatorModel
from presenter.pathCreatorPresenter import PathCreatorPresenter
from view.pathCreatorView import PathCreatorView

from model.frameworkModel import FrameworkModel
from view.frameworkView import FrameworkView
from presenter.frameworkPresenter import FrameworkPresenter

def main():
    # pathModel = PathCreatorModel()
    # pathView = PathCreatorView()
    # pathPresenter = PathCreatorPresenter(pathView, pathModel)

    frameworkModel = FrameworkModel()
    frameworkView = FrameworkView()
    frameworkPresenter = FrameworkPresenter(frameworkView, frameworkModel)
    
    # repositorio = pathView.repositorio()

    language, extencion = frameworkPresenter.choose_languages()
    # LEMBRAR DE VER SE ESTÁ CHAMANDO A FUNÇAO DUAS VEZES

    
    # opcao = pathView.menu_inicial()

    # pathPresenter.create_arch(opcao, extencion, repositorio)



if __name__ == "__main__":
    main()