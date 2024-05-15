import flet as ft
from Views.ViewFamiliar import ViewFamiliar

class ViewLogin():
    def __init__(self,page: ft.Page):
        self.page = page
        self.dlg = ft.AlertDialog(
            modal=True,
            title=ft.Text("Alerta"),
            content=ft.Text("Sus credenciales no estan registradas"),
            actions=[
                ft.TextButton("aceptar", on_click=self.close_dlg),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )
        self.username = ft.TextField(
            label="Usuario",
            helper_text="Ingrese su nombre de usuario",
            border_radius=ft.BorderRadius(5, 5, 5, 5),
            width=200,
            color=ft.colors.WHITE
        )

        self.password = ft.TextField(
            label="Contraseña",
            helper_text="Ingrese su contraseña",
            password=True,
            can_reveal_password=True,
            border_radius=ft.BorderRadius(5, 5, 5, 5),
            width=200,
            color=ft.colors.WHITE
        )
    def close_dlg(self,e):
            self.dlg.open = False
            self.page.update()
    def checkUser(self,e):
        if(self.username.value == "admin"  and self.password.value == "123456"):
            ventana = ViewFamiliar(self.page)
            self.page.views.append(ventana.getViewFamiliar())
           
        else:
            print("acceso denegado")
            self.page.dialog = self.dlg
            self.dlg.open = True
            self.username.value = ""
            self.password.value = ""
        
        self.page.update()

    def getViewLogin(self):
        
        logo_text = ft.Text("MediTrack", size=28,text_align=ft.TextAlign.CENTER,color=ft.colors.WHITE)
        iniciarText =  ft.Text("Iniciar Sesion", size=18,text_align=ft.TextAlign.CENTER,color=ft.colors.WHITE,style=ft.TextThemeStyle.HEADLINE_MEDIUM)
        
        userImg=ft.Image(
            src="img/loginUser.png",
            height=45,
            width=45

        )
        passImg = ft.Image(
            src="img/loginPass.png",
            height=45,
            width=45

        )



        # Botón de iniciar sesión
        login_button = ft.ElevatedButton(
            text="Iniciar Sesión",
            on_click=self.checkUser,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=5),
                color=ft.colors.BLUE,     
            ),
            width=200
        )

        user = ft.Row(
            controls=[
                userImg,
                self.username
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )
        passw = ft.Row(
            controls=[
                passImg,
                self.password,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )
        content =  ft.Column(
            [ft.Container(height=5),
                ft.Column(controls=[
                    logo_text,
                ft.Image(src="img/Logo.png", height=200, expand=True),
                iniciarText
                
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            height=220,
            spacing=15
            ),

                ft.Column(
                    [
                        ft.Column(
                                [
                               user

                                ],
                                spacing=0,
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                        
                        ft.Container(width=50),
                        ft.Column(
                                [
                                passw,
                                login_button
                                
                                ],
                               alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            )
                        
                    ],
                    #spacing=50,
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    expand=True
                
                ),

            ],
            spacing=80,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
            width=self.page.width,
            height=self.page.height,
            
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

        return ft.View(
            route="/Inicio",
            controls=[
                ft.Stack(
                    [
                        background,
                        content
                    ]
                )
            ],
            padding=0
        )