import flet as ft
from src.model.usuario_model import Usuario

class DespesaUsuarioView(ft.View):
    def __init__(self,pagina:ft.Page):
        super().__init__()
        
        self.pagina = pagina
        self.route = "/despesas"
        self.bgcolor ="#DFEBE4"
        self.horizontal_alignment ="center"
        dados_usuario = pagina.session.store.get("usuario_logado")
        self.login = dados_usuario.get("login")
        

        titulo = ft.Text(value="Despesas",
                        size = 25,
                        font_family="Georgia",
                        weight=ft.FontWeight.BOLD,
                        color="#395F4A")

        titulo_com_linhas = ft.Row(alignment="center",
                                                   vertical_alignment="center", 
                                                   controls=[ft.Container(expand=True,
                                                                          height=1.5,
                                                                          bgcolor="#395F4A"),
                                                                          ft.Container(content=titulo),
                                                                          ft.Container(expand=True,
                                                                                       height=1.5,
                                                                                       bgcolor="#395F4A")],
                                                                                       margin=ft.Margin.only(bottom=60))

        lista_despesas = []
        #pegar as despesas, percorrer as despesas, crias a lista despesas 

        tabela_despesas = ft.DataTable(columns=[ft.DataColumn(label="id da Despesa"),
                                                ft.DataColumn(label="Descrição"),
                                                ft.DataColumn(label="Valor"),
                                                ft.DataColumn(label="Data"),
                                                ft.DataColumn(label="Categoria")],
                                                rows=[ft.DataRow()
                                                ])
        
        self.controls =[titulo_com_linhas]
    