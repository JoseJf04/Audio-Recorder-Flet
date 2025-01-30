import flet as ft

# Botón Micrófono
class MicButton(ft.IconButton):
    def __init__(self, bgcolor, color, size, on_click):
        super().__init__()
        self.icon =  ft.icons("mic")
        self.bgcolor = bgcolor
        self.icon_color = color
        self.icon_size = size
        self.on_click = on_click

    # Metodo para actualizar el color de fondo y color icono del boton
    def update_icon_button_color(self, bgcolor, color):
        self.bgcolor = bgcolor
        self.icon_color = color

# Texto basico
class BasicText(ft.Text):
    def __init__(self, value, color, font, size):
        super().__init__()
        self.value = value
        self.color = color
        self.font_family = font
        self.size = size
