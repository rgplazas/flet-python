import flet as ft

class what_to_do_app(ft.UserControl):
    def build(self):
        # Elementos en la vista
        self.new_task = ft.TextField(hint_text="¿Qué hay que hacer?", expand=True)
        self.tasks = ft.Column()
        
        # Control raíz de la aplicación (es decir, "vista") que contiene todos los demás controles
        # Column control que se utiliza para colocar sus controles secundarios verticalmente en una página
        # Row control que se utiliza para colocar sus controles secundarios horizontalmente en una página
        # Contedor en columna de toda la app
        
        return ft.Column(
            width=600,
            #Contenedor de agregacion de tareas
            controls=[
                ft.Row( # row con TextField y FloatingActionButton
                    controls=[
                        self.new_task,
                        ft.FloatingActionButton(icon=ft.icons.ADD, on_click=self.add_clicked),
                    ],
                ),
                #Contenedor de tareas
                #Cuerpo de tarea agregada ordenada en columnas 
                self.tasks,
            ],
    )

    def add_clicked(self, e):
        self.tasks.controls.append(ft.Checkbox(label=self.new_task.value))
        self.new_task.value = ""
        self.update()