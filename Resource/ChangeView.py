import flet as ft

class ChangeView():
    
    def __init__(self,page):
        self.page = page
        self.fotoFondo ='https://i.postimg.cc/HskYYR5B/VENTANA2-FONDO.png'
    
    def Navegacion(self,destination: ft.ControlEvent):
  
        if destination.data == "0":
            self.page.views.clear()
            
            self.page.views.append(self.paginaSelectionTipo.getPaginaSelectionTipo())
        
        elif destination.data == "1":
            self.page.views.clear()
            self.page.views.append(self.paginaSelection.getPaginaSelection()
            )
        
        
        self.page.update()
