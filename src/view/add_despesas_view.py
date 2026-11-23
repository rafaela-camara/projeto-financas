import flet as ft
from src.model.usuario_model import Usuario
from src.model.categoria_model import Categoria
from src.model.despesa_model import Despesa
from datetime import datetime
class AddDespesaUsuarioView(ft.View):
    def __init__(self,pagina:ft.Page):
        super().__init__()
        
        self.pagina = pagina
        self.route = "/add_despesas"
        self.bgcolor ="#DFEBE4"
        self.horizontal_alignment ="center"
        dados_usuario = pagina.session.store.get("usuario_logado")
        self.login = dados_usuario.get("login")
        

        titulo = ft.Text(value="Adicionar Despesas",
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
                                                                               bgcolor="#395F4A")],
                                                                               margin=ft.Margin.only(bottom=60))

        self.descricao = ft.TextField(label="Descrição",
                                border_color="#609E7C",
                                border_radius=10,
                                border_width=2.5,
                                margin=10,
                                width=550)

        self.valor = ft.TextField(label="Valor",
                                border_color="#609E7C",
                                border_radius=10,
                                border_width=2.5,
                                margin=10,
                                width=550)

        self.data = ft.TextField(label="Data",
                                border_color="#609E7C",
                                border_radius=10,
                                border_width=2.5,
                                margin=10,
                                width=550)
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
                                options= opcoes_cat)
        botao_add = ft.Button(content="Adicionar",
                      color="#263F31",
                      bgcolor="#9FC5B0",
                      width=200,
                      on_click=self.add)
        self.controls =[titulo_com_linhas,
                        self.descricao,
                        self.valor,
                        self.data,
                        self.categoria,
                        botao_add]
    def add(self):
        valor_descricao = self.descricao.value
        valor_valor = self.valor.value
        valor_data = self.data.value
        data_convertida = datetime.strptime(valor_data, "%d/%m/%Y").date()
        id_categoria = self.categoria.value
        login = self.login

        resultado = Despesa().incluir(login,id_categoria,valor_descricao, valor_valor, data_convertida )

        if resultado:
            self.pagina.show_dialog(ft.SnackBar(ft.Text("Cadastro efeituado com sucesso!"), bgcolor="#21a517"))
        else:
            self.pagina.show_dialog(ft.SnackBar(ft.Text("Erro ao cadastrar. Entre em contato com o adiministrador"), bgcolor="#e0101f"))

        if self.descricao == "" or self.valor == "" or self.data == "" or self.categoria == "":
            self.pagina.show_dialog(ft.SnackBar(ft.Text("Peencha todos os campos"), bgcolor="#1A1AB6"))
        self.descricao.value = ""
        self.valor.value = ""
        self.data.value = ""
        self.categoria = ""
        self.pagina.update()
        
