import flet as ft
from src.view.cadastro_usuario_view import CadastroUsuarioView
from src.view.login_usuario_view import LoginUsuarioView
from src.view.principal_usuario_view import PrincipalUsuarioView
from src.view.add_despesas_view import AddDespesaUsuarioView
from src.view.despesas_view import DespesaUsuarioView
from src.view.despesa_categoria_view import DespesaCategoriaUsuarioView
from src.view.categoria_view import CategoriaUsuarioView

def main(pagina:ft.Page):

    def navegacao(componente):
        item_clicado = componente.control.selected_index
        if item_clicado == 0 :
            pagina.navigate("/principal")
        elif item_clicado == 1 :
                pagina.navigate("/categoria")
        elif item_clicado == 2:
            pagina.navigate("/add_despesas")
        elif item_clicado == 3:
            pagina.navigate("/despesas")
        elif item_clicado == 4:
            pagina.navigate("/despesas_categoria")
        elif item_clicado == 5:
            pagina.navigate("/login")
        




    barra_navegacao = ft.NavigationBar(destinations=[
                                        ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Principal"),
                                        ft.NavigationBarDestination(icon=ft.Icons.CATEGORY_ROUNDED, label="Categoria"),
                                        ft.NavigationBarDestination(icon=ft.Icons.ADD_SHOPPING_CART, label="Adicionar Despesas"),
                                        ft.NavigationBarDestination(icon=ft.Icons.ATTACH_MONEY, label="Despesas"),
                                        ft.NavigationBarDestination(icon=ft.Icons.FEED_OUTLINED, label="Despesas por Categoria"),
                                        ft.NavigationBarDestination(icon=ft.CupertinoIcons.SQUARE_ARROW_RIGHT, label="Sair"),],
                                        on_change=navegacao)

    
    def roteamento(e=None):
        pagina.views.clear()

        if pagina.route == "/cadastro":
            tela_cadastro_usuario = CadastroUsuarioView(pagina)
            tela_login_usuario = LoginUsuarioView(pagina)
            pagina.views.append(tela_cadastro_usuario)

        elif pagina.route == "/login":
            tela_login_usuario = LoginUsuarioView(pagina)
            pagina.views.append(tela_login_usuario)

        elif pagina.route == "/principal":
            tela_principal_usuario = PrincipalUsuarioView(pagina)
            tela_principal_usuario.navigation_bar = barra_navegacao
            pagina.views.append(tela_principal_usuario)

        elif pagina.route == "/add_despesas":
            tela_add_despesas = AddDespesaUsuarioView(pagina)
            tela_add_despesas.navigation_bar = barra_navegacao
            pagina.views.append(tela_add_despesas)

        elif pagina.route == "/despesas":
            tela_despesas = DespesaUsuarioView(pagina)
            tela_despesas.navigation_bar = barra_navegacao
            pagina.views.append(tela_despesas)

        elif pagina.route == "/despesas_categoria":
            tela_categoria_despesa = DespesaCategoriaUsuarioView(pagina)
            tela_categoria_despesa.navigation_bar = barra_navegacao
            pagina.views.append(tela_categoria_despesa)

        elif pagina.route == "/categoria":
            tela_categoria = CategoriaUsuarioView(pagina)
            tela_categoria.navigation_bar = barra_navegacao
            pagina.views.append(tela_categoria)


        pagina.update()

    # quando a pagina mudar de rota
    pagina.on_route_change = roteamento
    roteamento()
    pagina.navigate("/categoria")

ft.run(main)