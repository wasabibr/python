#!/usr/bin/env python
# coding: utf-8

# # Automação de Sistemas e Processos com Python
# 
# ### Desafio:
# 
# Todos os dias, o nosso sistema atualiza as vendas do dia anterior.
# O seu trabalho diário, como analista, é enviar um e-mail para a diretoria, assim que começar a trabalhar, com o faturamento e a quantidade de produtos vendidos no dia anterior
# 
# E-mail da diretoria: seugmail+diretoria@gmail.com<br>
# Local onde o sistema disponibiliza as vendas do dia anterior: https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing
# 
# Para resolver isso, vamos usar o pyautogui, uma biblioteca de automação de comandos do mouse e do teclado

# In[38]:


# !pip install pyautogui


# In[39]:


import pyautogui
import pyperclip
import time

pyautogui.PAUSE = 1

# pyautogui.click -> clicar
# pyautogui.write -> escrever
# pyaytogui.press -> pressionar
# pyautogui.hotkey -> atalho


# Passo 1: Entrar no sistema da empresa (no link do drive)

pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

time.sleep(5)

# Observação: Se tivermos que iniciar um aplicativo do zero, utilizaremos uma sequência de comandos similar ao que se segue:
# pyautogui.press("win")
# pyautogui.write("chrome")
# pyautogui.press("enter")


# Passo 2: Navegar até o local do relatório (entrar na pasta Esportar)
pyautogui.click(x=354, y=305, clicks=2)
time.sleep(2)


# Passo 3: Expostar relatório (fazer o download)
pyautogui.click(x=347, y=305) # clicar no arquivo, o parâmetro button="right", faz com que o click seja com o botão direito
pyautogui.click(x=1160, y=189) # clicar nos 3 pontinhos
pyautogui.click(x=1000, y=592) # clicar no fazer download
time.sleep(5) # esperar o download acabar


# ### Vamos agora ler o arquivo baixado para pegar os indicadores
# 
# - Faturamento
# - Quantidade de Produtos

# In[40]:


# Passo 4: Calcular os indicadores (faturamento e quantidade de produtos)
import pandas as pd

tabela = pd.read_excel(r"C:\Users\Jefferson\Downloads\Vendas - Dez.xlsx")
display(tabela)

faturamento = tabela["Valor Final"].sum()
print(faturamento)
quantidade = tabela["Quantidade"].sum()
print(quantidade)


# ### Vamos agora enviar um e-mail pelo gmail

# In[41]:


# Passo 5: Enviar um e-mail para a diretoria

# abrir aba
pyautogui.hotkey("ctrl", "t")

time.sleep(5)

# entrar no link do email - https://mail.google.com/mail/u/0/#inbox
pyperclip.copy("https://mail.google.com/mail/u/0/#inbox")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(5)

# clicar no botão escrever
pyautogui.click(x=92, y=199)
time.sleep(5)

# preencher as informações do e-mail
pyautogui.write("jefframosbr@gmail.com")
pyautogui.press("tab") # selecionar o email

pyautogui.press("tab") # pular para o campo de assunto
pyperclip.copy("Relatório de Vendas")
pyautogui.hotkey("ctrl", "v")

pyautogui.press("tab") # pular para o campo de corpo do email

texto = f"""
Prezados,

Segue relatório de vendas.
Faturamento: R${faturamento:,.2f}
Quantidade de produtos vendidos: {quantidade:,}

Qualquer dúvida estou à disposição.
Att.,
Jefferson
"""

# formatação dos números (moeda, dinheiro)

pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")

# enviar o e-mail
pyautogui.hotkey("ctrl", "enter")


# #### Use esse código para descobrir qual a posição de um item que queira clicar
# 
# - Lembre-se: a posição na sua tela é diferente da posição na minha tela

# In[42]:


time.sleep(5)
pyautogui.position()


# In[ ]:




