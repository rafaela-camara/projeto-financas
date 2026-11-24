import flet as ft
from src.model.usuario_model import Usuario
from src.model.categoria_model import Categoria
from src.model.despesa_model import Despesa
class DespesaCategoriaUsuarioView(ft.View):
    def __init__(self,pagina:ft.Page):
        super().__init__()
        
        self.pagina = pagina
        self.route = "/despesas_categoria"
        self.bgcolor ="#DFEBE4"
        self.horizontal_alignment ="center"
        dados_usuario = pagina.session.store.get("usuario_logado")
        self.login = dados_usuario.get("login")
        

        titulo = ft.Text(value="Despesas por Categoria",
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
                                                                                               bgcolor="#395F4A")])

        self.lista_despesas = []
        opcoes_cat = []

        categorias = Categoria.recuperar_todos(self.login)
                
        for categoria in categorias:
            opcao = ft.DropdownOption(key=categoria.get("id_categoria"),
                                      text= categoria.get("tipo"))
            opcoes_cat.append(opcao)

        self.categoria = ft.Dropdown(label="categoria",
                                    border_color="#609E7C",
                                    border_radius=10,
                                    border_width=2.5,
                                    margin=10,
                                    width=550,
                                    options= opcoes_cat,
                                    on_select=self.atualizar_despesas)

        self.atualizar_despesas()

        
        
        self.lista_despesas = []
                 
        
        self.tabela_despesas = ft.DataTable(columns=[
                                                ft.DataColumn(ft.Text(value="ID Despesa",size=20,font_family="Georgia",weight=ft.FontWeight.BOLD)),
                                               
                                                ft.DataColumn(ft.Text(value="Descrição",size=20,font_family="Georgia",weight=ft.FontWeight.BOLD)),
                                                ft.DataColumn(ft.Text(value="Valor",size=20,font_family="Georgia",weight=ft.FontWeight.BOLD)),
                                                ft.DataColumn(ft.Text(value="Data",size=20,font_family="Georgia",weight=ft.FontWeight.BOLD)),
                                                ft.DataColumn(ft.Text(value="Excluir",size=20,font_family="Georgia",weight=ft.FontWeight.BOLD))],
                                                rows=self.lista_despesas)

        self.atualizar_despesas()
        self.controls =[titulo_com_linhas,
                        self.categoria,
                        self.tabela_despesas]
        
        
        
    def atualizar_despesas(self):
        self.lista_despesas.clear()
        self.id_categoria = self.categoria.value
        despesas = Despesa.recuperar_por_categoria(self.login, self.id_categoria)
        for despesa in despesas:
            id_despesa = str(despesa.get("id_despesa"))
            linha = ft.DataRow(cells=[
                                            ft.DataCell(id_despesa),
                                            
                                            ft.DataCell(ft.Text(str(despesa.get("descricao")),size=17,font_family="Georgia")),
                                            ft.DataCell(ft.Text(str(despesa.get("valor")),size=17,)),
                                            ft.DataCell(ft.Text(str(despesa.get("data")),size=17,)),
                                            ft.DataCell(ft.FloatingActionButton(icon=ft.Icon(icon=ft.Icons.DELETE_OUTLINE,
                                                                                                     color="#395F4A"),
                                                                                                     bgcolor="#9FC5B0",
                                                                                                     width=35,
                                                                                                     height=30,
                                                                                                     key=id_despesa,
                                                                                                     on_click=self.excluir_despesa
                                                                                                     ))])
        
            self.lista_despesas.append(linha)
        
        self.pagina.update()
        
    def excluir_despesa(self, botao):
                id_despesa = botao.control.key
                Despesa().excluir(id_despesa)
                self.atualizar_despesas()

       