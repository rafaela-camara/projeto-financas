import flet as ft
from src.model.usuario_model import Usuario
class CategoriaUsuarioView(ft.View):
    def __init__(self,pagina:ft.Page):
        super().__init__()
        
        self.pagina = pagina
        self.route = "/categoria"
        self.bgcolor ="#DFEBE4"
        self.horizontal_alignment ="center"
        
        self.vertical_alignment = "center"

        titulo = ft.Text(value="Página Categoria",
                        size = 25,
                        font_family="Georgia",
                        weight=ft.FontWeight.BOLD,
                        color="#395F4A")
        
        self.controls =[titulo]