#!/usr/bin/env python
# coding: utf-8

# # Criar Bot com Python
# 
# ### Bot no Computador - pyautogui

# In[1]:


import pyautogui

pyautogui.PAUSE = 2

# abrir a ferramenta/o sistema/o programa
pyautogui.press("win")
pyautogui.write("login.xlsx")
pyautogui.press("backspace")
pyautogui.press("enter")

# preencher o login
pyautogui.click(x=500, y=186)
pyautogui.write("lira")

# preencher a senha
pyautogui.click(x=511, y=225)
pyautogui.write("senha")

# clicar em fazer login
pyautogui.click(x=491, y=347)


# In[ ]:


# Para a incontrar a posição de cada campo, botão etc.
import time

time.sleep(3)
pyautogui.position()


# ### Bot na Internet - Selenium

# In[2]:


# Depois de instalar o Selenium, via prompt (pip install selenium), procurar um dos dois arquivos abaixo:
# chrome -> chromedriver
# firefox -> geckodriver

from selenium import webdriver
import time

navegador = webdriver.Chrome()
navegador.get("https://login.live.com/")
time.sleep(1)
navegador.find_element_by_xpath('//*[@id="i0116"]').send_keys("pythonimpressionador@outlook.com")
navegador.find_element_by_xpath('//*[@id="idSIButton9"]').click()

time.sleep(1)

navegador.find_element_by_xpath('//*[@id="i0118"]').send_keys("Python123123")
navegador.find_element_by_xpath('//*[@id="idSIButton9"]').click()


# In[ ]:




