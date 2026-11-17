import flet as ft
from src.model.usuario_model import Usuario
from src.model.categoria_model import Categoria
class CategoriaUsuarioView(ft.View):
    def __init__(self,pagina:ft.Page):
        super().__init__()
        
        self.pagina = pagina
        self.route = "/categoria"
        self.bgcolor ="#DFEBE4"
        self.horizontal_alignment ="center"
        dados_usuario = pagina.session.store.get("usuario_logado")
        self.login = dados_usuario.get("login")
        
        
        titulo = ft.Text(value="Categoria",
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


        self.texto_cadastrar = ft.TextField(label="Nova Categoria",
                                border_color="#609E7C",
                                border_radius=10,
                                border_width=2.5,
                                margin=10)

        botao_salvar = ft.Button(content="Salvar",
                      color="#263F31",
                      bgcolor="#9FC5B0",
                      width=100,
                      on_click=self.cadastrar_categoria)

        linha_cadastrar = ft.Row(controls=[self.texto_cadastrar,botao_salvar], width=450)

        container_cima = ft.Container(content=ft.Column(controls=[linha_cadastrar,],
                                                                  alignment="center",
                                                                  horizontal_alignment="center",),
                                                                  width=5000,)
                                                                  
        subtitulo_existente = ft.Text(value="Categorias Existentes",
                                size = 25,
                                font_family="Georgia",
                                weight=ft.FontWeight.BOLD,
                                color="#395F4A")

        self.lista_categorias = []


        container_baixo = ft.Container(content=ft.Column(controls=[subtitulo_existente,
                                                                   ft.Column(controls= self.lista_categorias)],
                                                                  alignment="center",
                                                                  horizontal_alignment="center",))

        
        self.atualizar_lista()

        self.controls =[titulo_com_linhas,
                        container_cima,
                        container_baixo,
                        ]


    def cadastrar_categoria(self):
        nome_categoria = self.texto_cadastrar.value
        resultado = Categoria().adicionar(tipo=nome_categoria, login=self.login)

        if resultado:
            self.pagina.show_dialog(ft.SnackBar(ft.Text("Cadastro efeituado com sucesso!"), bgcolor="#21a517"))
        else:
            self.pagina.show_dialog(ft.SnackBar(ft.Text("Erro ao cadastrar. Entre em contato com o adiministrador"), bgcolor="#e0101f"))

        self.atualizar_lista()
         
    def atualizar_lista(self):
        categorias = Categoria().recuperar_todos(self.login)
        self.lista_categorias.clear()

        for categoria in categorias:
            id_categoria = categoria.get("id_categoria")
            print(id_categoria)
            nome_categoria = categoria.get("tipo")
            botao_excluir = ft.FloatingActionButton(icon=ft.Icon(icon=ft.Icons.DELETE_OUTLINE,
                                                                                             color="#395F4A"),
                                                                                             bgcolor="#9FC5B0",
                                                                                             width=35,
                                                                                             height=30,
                                                                                             on_click=self.excluir,
                                                                                             key=id_categoria)
            campo_tipo = ft.TextField(value=nome_categoria,
                                      border_color="#609E7C",
                                      border_radius=10,
                                      border_width=2.5,
                                      text_align="center",
                                      read_only=True)
            linha = ft.Row(controls=[campo_tipo,botao_excluir],alignment=ft.MainAxisAlignment.CENTER)
            self.lista_categorias.append(linha)
        self.pagina.update()

    def excluir(self, e):
        id_categoria=e.control.key
        Categoria().excluir(id_categoria)
        self.atualizar_lista()