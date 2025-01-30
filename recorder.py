import pyaudio
import threading
import wave
import sounddevice as sd

# Class MicChecker
class MicChecker:
    # Metodo para chequear micrófonos conectados
    def check_devices(self):
        # Consulta los dispositivos de audio disponibles
        devices = sd.query_devices()

        # lista para los nombres de los micrófonos
        microphones = []

        # Iteración sobre los dispositivos encontrados
        for device in devices:
            # Verificar si el dispositivo tiene canales de entrada
            if device['max_input_channels'] > 0:
                # Convertir el nombre del dispositivo a minuscula
                device_name = device['name'].lower()
                # verifica si el nombre del dispositivo tiene terminos relacinados con micrófonos
                if any(term in device_name for term in ["mic", "microphone", "entrada"]):
                    # Agrega el nombre del micrófono a la lista
                    microphones.append(device_name)

        # Filtra los micrófonos excluyendo aquellos que contienen "line" o "capture" en su nombre
        filtered_microphones = [m for m in microphones if "line" not in m and "capture" not in m]

        # Devuelve True si se encontraron micrófonos válidos, de lo contrario devuelve False
        if filtered_microphones:
            return True
        else:
            return False


# Class Recoder
class Recorder:
    # Inicialización de la clase
    def __init__(self):
        self.is_recording = False # Estado de la grabación
        self.frames = [] # Lista de frames de audios

    # Metodo para iniciar la grabación
    def start_rec(self, FORMAT, CHANNELS, RATE, CHUNK):
        # Cabio de estado de grabación a True
        self.is_recording = True

        # Creación de la Instancia de PyAdio
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

        # Creación del hilo para grabar e inicio
        self.theread_recording = threading.Thread(target=self.record(CHUNK))
        self.theread_recording.start()

    # Metodo para grabar en bucle
    def record(self, CHUNK):
        # Mientras se está grabando
        while self.is_recording:
            # Leer datos del stream
            data = self.stream.read(CHUNK)

            # Almacenar los datos
            self.frames.append(data)

    # Medoto para detener la grabación
    def stop_rec(self, FILE_NAME, CHANNELS, FORMAT, RATE):
        # Cambia el estado de la grabación a False
        self.is_recording = False

        # Detener y cerrar el stream
        self.stream.stop_stream()
        self.stream.close()

        # Termina PyAdio
        self.p.terminate()

        # Creación del archivo de audio
        with wave.open(FILE_NAME, "wb") as wf:
            # Establecer Canales
            wf.setnchannels(CHANNELS)

            # Establecer tamaño de muestra
            wf.setsampwidth(self.p.get_sample_size(FORMAT))

            # Establecer tamaño de muestreo
            wf.setframerate(RATE)

            # Escribir los frames
            wf.writeframes(b''.join(self.frames))