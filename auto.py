from time import sleep
from datetime import date
import pyautogui
import pyperclip
import pandas as pd

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

pyautogui.PAUSE = 1

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
pyautogui.click(x=340, y=252, clicks=2)
sleep(2)

# Fazer o download
cliques([[340, 252, 1], [1733, 145, 1], [1545, 509, 1]])

sleep(5)

# Analisando os dados do Excel
tabela = pd.read_excel(r"C:\Users\T-GAMER\Downloads\Vendas - Dez.xlsx")

faturamento = tabela["Valor Final"].sum()
quantidade = tabela["Quantidade"].sum()

# Abrindo o Gmail
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://mail.google.com/mail/u/0/#inbox")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
sleep(5)

# Abrindo uma mensagem e colocando o destino
pyautogui.click(x=61, y=173)
pyautogui.write("testepythonauto@gmail.com")
pyautogui.press("tab")
pyautogui.press("tab")

# Escrevendo o email
pyperclip.copy("Relatório de Vendas")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")

dia = date.today().day
mes = date.today().month
ano = date.today().year

texto = f"""Prezados,

Segue relatório de vendas referente a {dia}/{mes}/{ano}.
Faturamento: {faturamento:,.2f}
Quantidade de produtos vendidos: {quantidade:,.2f}

Qualquer dúvida estou à disposição.
Att,
Isabelle Gomes"""

pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")

# Enviando o email
pyautogui.hotkey("ctrl", "enter")
