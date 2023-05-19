import serial
import pyautogui

puerto_serie = serial.Serial('COM5', 9600)  # Reemplaza 'COMX' con el puerto serie correcto
# Diccionario que mapea los datos recibidos a las acciones correspondientes
acciones = {
    '1': 'F13',
    '2': 'F14',
    '3': 'F15',
    'A': 'F16',
    '4': 'F17',
    '5': 'F18',
    '6': 'F19',
    'B': 'F20',
    '7': 'F21',
    '8': 'F22',
    '9': 'F23',
    'C': 'F24',
    # Agrega aquí más mapeos de teclas según sea necesario
}

while True:
    if puerto_serie.in_waiting > 0:
        dato = puerto_serie.readline().decode().rstrip()
        if dato in acciones:
            tecla = acciones[dato]
            pyautogui.press(tecla)
        print("Dato recibido:", dato)
        """
        if dato == '1':
            pyautogui.press('F13')
        elif dato == '2':
            pyautogui.press('F14')
        elif dato == '3':
            pyautogui.press('F15')
        elif dato == 'A':
            pyautogui.press('F16')
        elif dato == '4':
            pyautogui.press('F17')
        elif dato == '5':
            pyautogui.press('F18')
        elif dato == '6':
            pyautogui.press('F19')
        elif dato == 'B':
            pyautogui.press('F20')
        elif dato == '7':
            pyautogui.press('F21')
        elif dato == '8':
            pyautogui.press('F22')
        elif dato == '9':
            pyautogui.press('F23')
        elif dato == 'C':
            pyautogui.press('F24')
        """