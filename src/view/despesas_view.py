import flet as ft
from src.model.usuario_model import Usuario
from src.model.despesa_model import Despesa
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
                        size = 40,
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
                                                                                       bgcolor="#395F4A")])

        self.lista_despesas = []
        #pegar as despesas, percorrer as despesas, crias a lista despesas 

        tabela_despesas = ft.DataTable(columns=[ft.DataColumn(label="Usuario"),
                                                ft.DataColumn(label="id_categoria"),
                                                ft.DataColumn(label="Descricao"),
                                                ft.DataColumn(label="valor"),
                                                ft.DataColumn(label="data")],
                                                rows=self.lista_despesas)

        self.atualizar_despesas()
        self.controls =[titulo_com_linhas,
                        tabela_despesas]


    def atualizar_despesas(self):
        despesas = Despesa.recuperar_todos(self.login)

        for despesa in despesas:
            linha = ft.DataRow(cells=[
                                    ft.DataCell(ft.Text(str(despesa.get("login")))),
                                    ft.DataCell(ft.Text(str(despesa.get("id_categoria")))),
                                    ft.DataCell(ft.Text(str(despesa.get("descricao")))),
                                    ft.DataCell(ft.Text(str(despesa.get("valor")))),
                                    ft.DataCell(ft.Text(str(despesa.get("data"))))])

            self.lista_despesas.append(linha)

        self.pagina.update()