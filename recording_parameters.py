import pyaudio

# Fórmato de audio. En este caso, 16 bits por muestra (paInt16).
FORMAT = pyaudio.paInt16

# Número de canales de audio. 2 para audio estéreo.
CHANNELS = 2

# Tasa de muestreo en Hertz (Hz). 44100 Hz.
RATE = 44100

# Define el tamaño del bloque de datos de audio. 1024
CHUNK = 1024
