import flet as ft
from src.model.usuario_model import Usuario
class PrincipalUsuarioView(ft.View):
    def __init__(self,pagina:ft.Page):
        super().__init__()
        
        self.pagina = pagina
        self.route = "/principal"

        dados_usuario = pagina.session.store.get("usuario_logado")
        nome_usuario = dados_usuario.get("login")

        self.bgcolor ="#DFEBE4"
        self.horizontal_alignment ="center"
        
        self.vertical_alignment = "center"

        titulo = ft.Text(value=f"Seja Bem-vindo, {nome_usuario}",
                        size = 25,
                        font_family="Georgia",
                        weight=ft.FontWeight.BOLD,
                        color="#395F4A")
        
        self.controls =[titulo]

    