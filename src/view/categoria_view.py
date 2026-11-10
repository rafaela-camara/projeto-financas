import flet as ft
from src.model.usuario_model import Usuario
class CategoriaUsuarioView(ft.View):
    def __init__(self,pagina:ft.Page):
        super().__init__()
        
        self.pagina = pagina
        self.route = "/categoria"
        self.bgcolor ="#DFEBE4"
        self.horizontal_alignment ="center"
        
        titulo = ft.Text(value="Categoria",
                        size = 40,
                        font_family="Georgia",
                        weight=ft.FontWeight.BOLD,
                        color="#395F4A")
        
        titulo_com_linhas = ft.Row(alignment="center",
                                   vertical_alignment="center", 
                                   controls=[ft.Container(expand=True,
                                                          height=1,
                                                          bgcolor="#395F4A"),
                                                          ft.Container(content=titulo),
                                                          ft.Container(expand=True,
                                                                       height=1,
                                                                       bgcolor="#395F4A")])

        subtitulo_cadastrar = ft.Text(value="Cadastre sua Categoria",
                        size = 25,
                        font_family="Georgia",
                        weight=ft.FontWeight.BOLD,
                        color="#395F4A")

        texto_cadastrar = ft.TextField(label="Nova Categoria",
                                border_color="#609E7C",
                                border_radius=10,
                                border_width=2.5,
                                margin=10)

        botao_salvar = ft.Button(content="Salvar",
                      color="#263F31",
                      bgcolor="#9FC5B0",
                      width=100,)

        linha_cadastrar = ft.Row(controls=[texto_cadastrar,botao_salvar], width=450)

        container_cima = ft.Container(content=ft.Column(controls=[subtitulo_cadastrar,
                                                                  linha_cadastrar,],
                                                                  alignment="center",
                                                                  horizontal_alignment="center",),
                                                                  width=5000,)
                                                                  
        subtitulo_existente = ft.Text(value="Categorias Existentes",
                                size = 25,
                                font_family="Georgia",
                                weight=ft.FontWeight.BOLD,
                                color="#395F4A")

        container_baixo = ft.Container(content=ft.Column(controls=[subtitulo_existente],
                                                                  alignment="center",
                                                                  horizontal_alignment="center",),
                                                                  width=5000,)






        
        self.controls =[titulo_com_linhas,
                        container_cima,
                        container_baixo]