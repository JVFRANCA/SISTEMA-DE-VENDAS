import flet as ft
#scroll=ft.ScrollMode.AUTO
def main(page: ft.Page):
    page.title = "SISTEMA PARA GESTAO DE VENDAS"
    page.window_width = None
    page.window_height = None
    page.window_maximized = True
    page.window_resizable = True
    page.window_minimizable = True
    page.window_maximizable = True



#-------------------LOGIN-----------------------------------------------------------------------------------------------------------
    def erro_login(e):
        page.dialog = alerta
        alerta.open = True
        page.update()

    alerta = ft.AlertDialog(
        title=ft.Text("Atenção!"),
        content=ft.Text("Dados invalidos! Tente Novamente")
    )

    def acessar_sistema(e):
        login_informado = informar_login.value
        senha_informada = informar_senha.value 
        if login_informado == "" and senha_informada == "":
            page.controls.clear()
            page.update()
        else:
            erro_login(e=erro_login)


    informar_login = ft.TextField(text_align="center", border_radius=10, border_color=ft.colors.BLUE)
    informar_senha = ft.TextField(password=True, can_reveal_password=True, text_align="center", border_radius=10, border_color=ft.colors.BLUE)

    lado_esquedo = ft.Container(
        content=ft.Column(
            controls=[
                ft.Image(
                    src=f"https://www.rech.com.br/blog/wp-content/uploads/2021/07/erp-siger-canais-de-vendas-700x428.jpg",
                    height=page.height,
                    width=page.width,
                    fit=ft.ImageFit.COVER
                )
            ],
            expand=True,
            alignment="center",
            # scroll=ft.ScrollMode.AUTO
        ),
        expand=True,
        padding=0,
        margin=0
    )

    lado_direito = ft.Container(
        content=ft.Column(
            controls=[
                # ft.Container(
                #     width=500,
                #     padding=ft.padding.only(bottom=50, top=50, left=150),
                #     content=ft.Column(
                #         controls=[
                #             ft.Image(
                #                 src=f"logo.jpg",
                #                 fit=ft.ImageFit.COVER
                #             )
                #         ],
                #     ),
                # ),
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Container(
                                content=ft.Text("AREA DE ACESSO", size=28),
                                padding=ft.padding.only(bottom=50, top=50, left=90),
                                width=400
                            ),
                            ft.Container(
                                content=ft.Text("INSIRA SEU LOGIN:"),
                                width=400
                            ),
                            ft.Container(
                                content=informar_login,
                                width=400
                            ),
                            ft.Container(
                                content=ft.Text("INSIRA SUA SENHA:"),
                                width=400
                            ),
                            ft.Container(
                                content=informar_senha,
                                width=400
                            ),
                            ft.Container(
                                content=ft.ElevatedButton(text="ACESSAR", color=ft.colors.BLACK, bgcolor=ft.colors.WHITE, on_click=acessar_sistema),
                                width=400,
                                padding=ft.padding.only(bottom=50)
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment="center"
                    ),
                    border=ft.border.all(2, ft.colors.PURPLE),
                    border_radius=10,
                    width=500,
                )
            ],
            expand=True,
            alignment="center",
            scroll=ft.ScrollMode.AUTO,
            horizontal_alignment="center"
        ),
        expand=True,
        padding=0,
        margin=0
    )

    janela = ft.Row(
        controls=[
            lado_esquedo,
            lado_direito
        ],
        expand=True,
        spacing=0,
    )

#-------------------LOGIN-----------------------------------------------------------------------------------------------------------    
    page.add(janela)

    page.update()
ft.app(target=main)    