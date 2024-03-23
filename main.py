import keyboard
import subprocess
import pyfiglet
from colorama import Fore
ASCII_art_1 = pyfiglet.figlet_format("Josefas")
ASCII_art_2 = pyfiglet.figlet_format("War Thunder")
print(Fore.BLUE + "Miguelki Presenta: ")
print(Fore.BLUE + "Josefas War Thunder Rage Quit Detector")
print(Fore.BLUE + ASCII_art_1)
print(Fore.BLUE + ASCII_art_2)
print(Fore.BLUE + "Esperando a el Rage Quit...")
print(Fore.BLUE + "Nota: Para cerrar el programa de forma correcta presiona la tecla F10")
def on_key_event(event):
    if keyboard.is_pressed('alt') and keyboard.is_pressed('f4'):
        # Ejecutar el comando deseado
        print("Rage quit detectado, abriendo War Thunder...")
        subprocess.run("cmd /c start steam://run/236390")

# Registrar el controlador de eventos para Alt + F4
keyboard.on_press(on_key_event)

# Mantener el programa en ejecución
keyboard.wait('f10')  # Espera hasta que se presione la tecla "Esc" para salir

