import flet as ft
from what_to_do import what_to_do_app as wtda

def main(page: ft.Page):
    
    page.title = "Que Hacer App"    
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add()

    # Crear instancia de aplicación
    what_to_do = wtda()

    # Agregar el control raíz de la aplicación a la página
    page.add(what_to_do)

ft.app(target=main, view=ft.WEB_BROWSER)