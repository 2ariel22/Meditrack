import flet as ft

class ViewInicio():


    def __init__(self,page: ft.Page):
        self.page = page

    def getViewInicio(self):
        title = ft.Text(
            value="Iniciar Sesión",
            style=ft.TextThemeStyle.HEADLINE_MEDIUM,
        )

        # Campo de usuario
        username = ft.TextField(
            label="Usuario",
            helper_text="Ingrese su nombre de usuario",
            border_radius=ft.BorderRadius(5, 5, 5, 5),
        )

        # Campo de contraseña
        password = ft.TextField(
            label="Contraseña",
            helper_text="Ingrese su contraseña",
            password=True,
            can_reveal_password=True,
            border_radius=ft.BorderRadius(5, 5, 5, 5),
        )

        # Botón de iniciar sesión
        login_button = ft.ElevatedButton(
            text="Iniciar Sesión",
            on_click=lambda _: print("Usuario:", username.value, "Contraseña:", password.value),
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=5),
                color=ft.colors.BLUE,
            ),
        )

        # Contenedor principal centrado
        content = ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                title,
                ft.Container(padding=10),
                username,
                ft.Container(padding=10),
                password,
                ft.Container(padding=20),
                login_button,
            ],
                
        )

        background_image = ft.Image(
            src="img/fondo.png",
            width=self.page.width,
            height=self.page.height,
            fit=ft.ImageFit.FILL,
            opacity=1,
        )

        background = ft.Container(
            content=background_image,
            width=self.page.width,
            height=self.page.height,
            bgcolor=ft.colors.BLUE_600,
            alignment=ft.alignment.center,
            padding=0,
            margin=0
        )

        contenido = ft.Container(
            content=ft.Container(
                content=content,
                padding=20,
                #bgcolor=ft.colors.WHITE,
                border_radius=10,
                alignment=ft.alignment.center,
            ),
            padding=0,
            bgcolor=ft.colors.BLUE_200,
            margin=ft.margin.only(top=100)
        )

        # Contenedor resaltado en el centro
        return ft.View(
            route="/Inicio",
            controls=[
                ft.Stack(
                    [
                    background,
                    ft.Row(
                        controls=[
                            contenido
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    )]
                    )
                    ],
                    padding=0
        )
            