# Grabadora de Audio

Este proyecto permite a los usuarios realizar capturas de audio y registrarlas 
en archivos .wav mediante una interfaz sencilla e intuitiva.

## Características:
    
*   **Diseño intuitivo y moderno**
*   **Interfaz simple y facil de utilizar**
*   **Deteccion de dispositivos de entrada de audio**
*   **Grabacion de audios sin limite de tiempo**
*   **Registro de audios en archivos .wav**

## Instalación:

1.  **Clona el repositorio:**
    ```bash
    git clone https://github.com/JoseJf04/Audio-Recorder-Flet
    cd <repository_directory>
    ```
2.  **Crear entórno virtual:**
*  **Windows:**
    ```bash
    python -m venv environment_name
    ```
*  **Linux:**
    ```bash
    python3 -m venv environment_name
    ```
3.  **Activa el entorno virtual:**
*  **Windows:**
    ```bash
    environment_name\Scripts\activate
    ```
*  **Linux:**
    ```bash
    source environment_name/bin/activate
    ```
4.  **Instala dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

## Ejecución:
* **Windows**
    ```bash
    python -m app.py
    ```
* **Linux**
    ```bash
    python3 -m app.py
    ```
## Estructura del proyecto
*   `app.py`: El módulo principal de Python que contiene la interfaz gráfica y las funciones que permiten iniciar o detener la grabación.
*   `widgets.py`: Contiene las clases para instanciar elementos de GUI en flet
*   `recorder.py`: Contiene las definiciones de las clases asociadas a permitir y gestionar la entrada de audio mediante dispositivos de entrada de audio
*   `recording_parameters.py`: Contiene definidos los parametros necesarios para la captura de audio




