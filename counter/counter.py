import flet as ft


def main(page: ft.Page):

    page.title = "Mi Contador con Flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    text_numbre  = ft.TextField(value=0, text_align=ft.TextAlign.CENTER, width=100, read_only=True)
    text_tiulo_1 = ft.Text(value="Hola, Soy un Contador en Desarrollo!", text_align=ft.TextAlign.CENTER)
    
    def minus(e):
        text_numbre.value = str(int(text_numbre.value) - 1)
        page.update()

    def plus(e):
        text_numbre.value = str(int(text_numbre.value) + 1)
        page.update()
    
    page.add(
        
        ft.Row(
            [
                text_tiulo_1
            ],
            alignment= ft.MainAxisAlignment.CENTER
        ),

        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click= minus),
                text_numbre,
                ft.IconButton(ft.icons.ADD, on_click= plus),
            ],
            alignment= ft.MainAxisAlignment.CENTER
        )
    )


# ft.app(main) #Aplicacion de Escritorio por defecto

ft.app(main, view=ft.WEB_BROWSER) #Aplicacion de Web