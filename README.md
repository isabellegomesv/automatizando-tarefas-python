# Automatizando envio de Relatórios com Python
Esse projeto tem como objetivo automatizar o envio de um relátorio diário de vendas, utilizando a biblioteca ***pyautogui*** para controlar o mouse e teclado do computador, simulando entrar em um sistema abrindo o chrome e entrando no drive e baixando uma planilha Excel depois analisando os dados com o ***pandas***, por fim enviando um relatório por email.

## Bibliotecas Necessárias
Para rodar esse projeto será necessário baixar algumas bibliotecas do Python como:
```
# Pyautogui
pip install pyautogui

# Pandas
pip install pandas

# Numpy
pip install numpy

# Openpyxl - 
pip install openpyxl
``` 
## Compatibilidade
Como essa automaização utiliza as coordenadas do mouse, para funcionar em diferentes telas será preciso uma adaptação, sendo assim o arquivo [pos.py](https://github.com/isabellegomesv/automatizando-tarefas-python/blob/master/pos.py) ajudará a achar essas coordenadas.

## Tecnologias Utilizadas
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original-wordmark.svg" width="80px" height="80px"/>  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original-wordmark.svg" width="75px" height="75px"/>
          
          
