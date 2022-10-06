import pyautogui
import pyperclip
from time import sleep

pyautogui.PAUSE = 1

def cliques(lista):
    '''
    A função cliques pode ser utilizada quando tem 2 ou mais cliques em seguida.
    Para utilizar essa função coloque em uma lista aninhada ([[0, 1, 2]]) onde as posições 
    correspondem a:
    0: posição do eixo x
    1: posição do eixo y
    2: quantidade de cliques
    '''
    for c in lista:
        pyautogui.click(x=c[0], y=c[1], clicks=c[2])

# Abrindo o chrome
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press("enter")

# Maximizando a aba do chrome e clicando na barra de pesquisa
sleep(1)
cliques([[1505, 155, 1], [268, 50, 1]])

# Entrando no drive
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga")
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

# Abrir a pasta
sleep(5)
pyautogui.click(x=337, y=248, clicks=2)
sleep(2)

# Fazer o download
cliques([[337, 248, 1], [1733, 145, 1], [1545, 509, 1]])

sleep(5)
