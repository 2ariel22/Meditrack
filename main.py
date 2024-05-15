import flet as ft
from Views.ViewInicio import ViewInicio


def main(page: ft.Page):
    page.bgcolor = ft.colors.BLUE_200
    page.padding=0
    page.title = "MediTrack"
    #page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER


    ventanda = ViewInicio(page)
    page.views.append(ventanda.getViewInicio())
    
    page.update()

ft.app(target=main)