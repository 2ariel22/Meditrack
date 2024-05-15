import flet as ft
from Views.ViewLogin import ViewLogin


class ViewInicio():
    def __init__(self,page: ft.Page):
        self.page = page

    def changeView(self,e):
        ventana = ViewLogin(self.page)
        self.page.views.append(ventana.getViewLogin())
        self.page.update()
        

    def getViewInicio(self):
        personal_icon = ft.Image(src="img/logoBoton.png",height=38)
        familiar_icon = ft.Image(src="img/logoBoton.png",height=38)

        personal_text = ft.Text("Personal de la salud", size=18,text_align=ft.TextAlign.CENTER,color=ft.colors.WHITE)
        familiar_text = ft.Text("Familiar", size=18,text_align=ft.TextAlign.CENTER,color=ft.colors.WHITE)
        logo_text = ft.Text("MediTrack", size=28,text_align=ft.TextAlign.CENTER,color=ft.colors.WHITE)
        content =  ft.Column(
            [ft.Container(height=5),
                ft.Column(controls=[
                    logo_text,
                ft.Image(src="img/Logo.png", height=200, expand=True),
                
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            height=250
            ),

                ft.Column(
                    [
                        ft.Column(
                                [ft.Container(content=personal_text),
                                ft.Container(content=personal_icon,
                                            height=40,
                                            on_click=lambda _: print("Personal de la salud seleccionado"),
                                            padding=0,
                                            
                                        ),
                                ],
                                spacing=0,
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER
                            ),
                        
                        ft.Container(width=50),
                        ft.Column(
                                [ft.Container(content=familiar_text,alignment=ft.alignment.center),
                                ft.Container(
                                    content=familiar_icon,
                                    on_click=self.changeView,
                                    height=40,
                                    padding=0,
                                    alignment=ft.alignment.center
                        ),],
                                spacing=0,
                                alignment=ft.MainAxisAlignment.CENTER,
                            )
                        
                    ],
                    #spacing=50,
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    expand=True
                
                ),
            ],
            spacing=100,
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