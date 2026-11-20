from model.pathCreatorModel import PathCreatorModel
from presenter.pathCreatorPresenter import PathCreatorPresenter
from view.pathCreatorView import PathCreatorView

def main():
    model = PathCreatorModel()
    view = PathCreatorView()
    presenter = PathCreatorPresenter(view, model)

    while True:
        repositorio = view.repositorio()
        opcao = view.menu_inicial()
        extensao = view.extensao()
        if opcao == 0: break
        presenter.create_arch(opcao, extensao, repositorio)

if __name__ == "__main__":
    main()