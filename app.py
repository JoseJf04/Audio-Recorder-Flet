"""Grabadora de audio sencilla"""

import flet as ft
from recorder import MicChecker
from recorder import Recorder
import widgets as wgt
from recording_parameters import FORMAT, CHANNELS, RATE, CHUNK

# Declaración de la función que inicia la página
def main(page: ft.Page):
    # Modificación de la ventana
    page.title = "Grabadora de audios"
    page.bgcolor = "White"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.width = 600
    page.window.height = 600

    # Instancia del verificador de microfono
    mic_checker = MicChecker()

    # Instancia de la grabadora
    rec = Recorder()

    # Declaración de la función que inicia la grabación
    def star_recording(e):
        if mic_checker.check_devices():
            text_status.value = "Hay un  microfono conectado"
            page.update()
            if not rec.is_recording:
                mic_btn.update_icon_button_color("White", "Purple")
                text_status.value = "Grabando audio..."
                page.update()
                rec.start_rec(FORMAT, CHANNELS, RATE, CHUNK)
            else:
                rec.stop_rec("Grabacion.wav", CHANNELS, FORMAT, RATE)
                mic_btn.update_icon_button_color("Purple","White")
                text_status.value = "Grabacion finalizada"
                page.update()
        else:
            text_status.value = "No hay microfonos conetados... Conecte un microfono para grabar"
            page.update()

    # Boton para grabar
    mic_btn = wgt.MicButton(bgcolor="Purple", color="White", size="100", on_click=star_recording)
    # Text de estatus
    text_status = wgt.BasicText(value="Presiona el microfono para grabar", color="Purple", font="Arial", size=16)

    # Añadir los elementos mic_Btn y text_status a la página
    page.add(mic_btn, text_status)

ft.app(target=main)