import flet as ft
from task import task as tk

class what_to_do_app(ft.UserControl):
    def build(self):
        # Elementos en la vista
        self.new_task = ft.TextField(hint_text="¿Qué hay que hacer?", expand=True)
        self.tasks = ft.Column()

        self.filter = ft.Tabs(
            selected_index=0,
            on_change=self.tabs_changed,
            tabs=[ft.Tab(text="Todos"), ft.Tab(text="Activos"), ft.Tab(text="Completos")],
        )
        
        # Control raíz de la aplicación (es decir, "vista") que contiene todos los demás controles
        # Column control que se utiliza para colocar sus controles secundarios verticalmente en una página
        # Row control que se utiliza para colocar sus controles secundarios horizontalmente en una página
        # Contedor en columna de toda la app
        
        return ft.Column(
                width=1000,
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
                    ft.Column(
                        spacing=25,
                        controls=[
                        self.filter,    
                        self.tasks,    
                        ],
                    ),
                ],
            )

    def add_clicked(self, e):
        task = tk(self.new_task.value, self.task_status_change, self.task_delete)
        self.tasks.controls.append(task)
        self.new_task.value = ""
        self.update()
    
    def task_status_change(self, task):
        self.update()

    def task_delete(self, task):
        self.tasks.controls.remove(task)
        self.update()

    def update(self):
        status = self.filter.tabs[self.filter.selected_index].text
        for task in self.tasks.controls:
            task.visible = (
                status == "Todos"
                or (status == "Activos" and task.completed == False)
                or (status == "Completos" and task.completed)
            )
        super().update()
    
    def tabs_changed(self, e):
        self.update()