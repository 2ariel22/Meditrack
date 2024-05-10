import flet as ft
from Views.ViewInicio import ViewInicio
from Views.ViewLogin import ViewLogin
from Views.Login import ViewInicio
from Views.ViewFamiliar import ViewFamiliar

def main(page: ft.Page):
    page.bgcolor = ft.colors.BLUE_200
    page.padding=0
    page.title = "MediTrack"
    #page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER


    #ventanda = ViewInicio(page)
    #page.views.append(ventanda.getViewInicio())
    #ventana = ViewLogin(page)
    #page.views.append(ventana.getViewLogin())
    ventana = ViewFamiliar(page)
    page.views.append(ventana.getViewFamiliar())
    page.update()

ft.app(target=main)