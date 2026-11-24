import flet as ft
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

        tabela_despesas = ft.DataTable(columns=[
                                                ft.DataColumn(ft.Text(value="Categoria",size=20,font_family="Georgia",weight=ft.FontWeight.BOLD)),
                                                ft.DataColumn(ft.Text(value="Descrição",size=20,font_family="Georgia",weight=ft.FontWeight.BOLD)),
                                                ft.DataColumn(ft.Text(value="Valor",size=20,font_family="Georgia",weight=ft.FontWeight.BOLD)),
                                                ft.DataColumn(ft.Text(value="Data",size=20,font_family="Georgia",weight=ft.FontWeight.BOLD)),
                                                ft.DataColumn(ft.Text(value="Excluir",size=20,font_family="Georgia",weight=ft.FontWeight.BOLD))],
                                                rows=self.lista_despesas)

        self.atualizar_despesas()
        self.controls =[titulo_com_linhas,
                        tabela_despesas]


    def atualizar_despesas(self):
        self.lista_despesas.clear()
        despesas = Despesa.recuperar_todos(self.login)
        
        for despesa in despesas:
            linha = ft.DataRow(cells=[
                                    ft.DataCell(ft.Text(str(despesa.get("tipo")),size=17,font_family="Georgia")),
                                    ft.DataCell(ft.Text(str(despesa.get("descricao")),size=17,font_family="Georgia")),
                                    ft.DataCell(ft.Text(str(despesa.get("valor")),size=17,)),
                                    ft.DataCell(ft.Text(str(despesa.get("data")),size=17,)),
                                    ft.DataCell(ft.FloatingActionButton(icon=ft.Icon(icon=ft.Icons.DELETE_OUTLINE,
                                                                                             color="#395F4A"),
                                                                                             bgcolor="#9FC5B0",
                                                                                             width=35,
                                                                                             height=30,
                                                                                             on_click=self.excluir_despesa,
                                                                                             key=self.login))])

            self.lista_despesas.append(linha)

        self.pagina.update()

    def excluir_despesa(self, botao):
        login = botao.control.key
        Despesa().excluir(login)
        self.atualizar_despesas()