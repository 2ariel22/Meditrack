import flet as ft

def main(page: ft.Page):
    page.title = "MediTrack"
    #page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    

    # Cargar imágenes desde enlaces externos
    personal_icon = ft.Image(src="img/logoBoton.png",height=38)
    familiar_icon = ft.Image(src="img/logoBoton.png",height=38)

    personal_text = ft.Text("Personal de la salud", size=18)
    familiar_text = ft.Text("Familiar", size=18)

    main_column = ft.Column(
        [ft.Container(height=5),
            ft.Row(controls=[
            ft.Image(src="img/Logo.png", height=200, expand=True),
            
        ], vertical_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER,
        
        ),

            ft.Column(
                [
                    ft.Column(
                            [personal_text,
                             ft.Container(content=personal_icon,
                                        height=40,
                                        on_click=lambda _: print("Personal de la salud seleccionado"),
                                        padding=0,
                                        
                                    ),
                             ],
                            spacing=0,
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                    
                    ft.Container(width=50),
                    ft.Column(
                            [familiar_text,
                             ft.Container(
                                content=familiar_icon,
                                on_click=lambda _: print("Familiar seleccionado"),
                                height=40,
                                padding=0
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
        width=page.width,
            height=page.height,
        
    )
    background_image = ft.Image(
            src="img/fondo.png",
            width=page.width,
            height=page.height,
            fit=ft.ImageFit.FILL,
            opacity=1,
        )

    background = ft.Container(
            content=background_image,
            width=page.width,
            height=page.height,
            bgcolor=ft.colors.BLUE_600,
            alignment=ft.alignment.center,
            padding=0,
            margin=0
        )

    page.add(ft.Stack(controls=[background,main_column]))

ft.app(target=main)