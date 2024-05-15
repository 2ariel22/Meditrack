import flet as ft

class ViewFamiliar():
    def __init__(self,page: ft.Page):
        self.page = page

    def getViewFamiliar(self):
       
        logo_text = ft.Text("MediTrack", size=28,text_align=ft.TextAlign.CENTER,color=ft.colors.WHITE)
        iniciarText = ft.Container(ft.Text("Familiar", size=16,text_align=ft.TextAlign.CENTER,
                                           color=ft.colors.BLACK,style=ft.TextThemeStyle.HEADLINE_MEDIUM),
                                           padding=10,
                                           border_radius=15,
                                           width=200,
                                           bgcolor=ft.colors.WHITE,
                                           expand=True)
        
        localizacionImg=ft.Image(
            src="img/Localizacion.png",
            height=100,
            width=100
        )
        
        localizacion = ft.Container(
            content=localizacionImg,
            height=100,
            width=100,
            padding=0
        )

        RegistroImg=ft.Image(
            src="img/registro.png",
            height=100,
            width=100
        )
        
        Registro = ft.Container(
            content=RegistroImg,
            height=100,
            width=100,
            padding=0
        )

        content =  ft.Column(
            [ft.Container(height=5),
                ft.Column(controls=[
                    logo_text,
                ft.Image(src="img/Logo.png", height=200, expand=True),
                ft.Row(controls=[
                    ft.Image(
            src="img/logoUsurio.png",
            height=35,
            width=35),iniciarText
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                width=250),
                
                
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            height=220,
            spacing=15
            ),

                ft.Column(
                    [
                        ft.Column(
                                [
                               localizacion,
                               ft.Text(value="Localizacion",color=ft.colors.WHITE)
                                ],
                                spacing=0,
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                
                            ),
                        
                        ft.Container(width=10, padding=0),
                        ft.Column(
                                [
                                Registro,
                                ft.Text(value="registro",color=ft.colors.WHITE)
                                ],
                               alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            )
                        
                    ],
                    spacing=10,
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.START,
                    expand=True
                
                ),

            ],
            spacing=40,
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