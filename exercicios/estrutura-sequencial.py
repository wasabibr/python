#!/usr/bin/env python
# coding: utf-8

# # Lista de Estrutura Sequencial

# #### 1. Faça um Programa que mostre a mensagem (print) "Alo mundo" na tela.

# In[1]:


print("Alo mundo")


# #### 2. Faça um Programa que peça um número (input) e então mostre a mensagem: "O número informado foi [número]."

# In[3]:


numero = input("O número informado foi: ")
print(f"O número informado foi {numero}.")


# #### 3. Faça um Programa que peça dois números e imprima a soma.

# In[5]:


num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
soma = num1 + num2
print(f"O somatório de {num1} e {num2} é {soma}.")


# #### 4. Faça um Programa que peça as 4 notas bimestrais de um aluno e mostre a média de todas as notas.

# In[8]:


nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f"A média das notas foi: {media}.")


# #### 5. Faça um Programa que converta metros para centímetros. Você pode pedir o comprimento em metros para o usuário (input).

# In[9]:


m = float(input("Digite o comprimento em m: "))
cm = m * 100

print (f"{m} m equivale a {cm} cm.")


# #### 7. Faça um Programa que calcule a área de uma sala de um apartamento. Para isso, o seu programa precisa pedir a largura da sala, o comprimento da sala e imprimir a área em m² da sala.

# In[12]:


l = float(input("Digite a largura da sala: "))
c = float(input("Digite o comprimento da sala: "))

a = l * c

print(f"A área da sala é: {a} m².")


# #### 8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

# In[13]:


val = float(input("Quanto você ganha por hora trabalhada: "))
horas = float(input("Quantas horas você trabalhou: "))

sal = val * horas

print(f"O seu salário neste mês foi de: {sal}")


# #### 9. Vamos criar um conversor de temperatura. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# $C = \frac{5}{9}(F-32)$

# In[16]:


f = float(input("Digite a temperatura em graus Fahrenheit: "))

c = 5 * (f - 32) / 9

print(f"{f} em graus Fahrenheit corresponde a {c} em graus Celsius.")


# #### 10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
# $F = \frac{9}{5}C + 32$

# In[17]:


c = float(input("Digite a temperatura em graus Celsius: "))

f = 5 / 9 * c + 32

print(f"{c} em graus Celsius corresponde a {f} em graus Fahrenheit.")


# # 12. Tendo como dados de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula:
# 
# $P = 72,7h - 58$
# 
# Lembrando que "algoritmo" nada mais é do que um programa, como todos os outros que você vem fazendo

# In[24]:


h = float(input("Digite a sua altura: "))

p = 72.7 * h - 58

print(f"O seu peso ideal é: {p}.")


# #### 13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# ##### a. Para homens: $P = 72,7h - 58$
# ##### b. Para mulheres: $P = 62,1h - 44,7$

# In[23]:


h = float(input("Digite uma altura: "))

ph = 72.7 * h - 58
pm = 62.1 * h - 47.7

print(f"Se a pessoa for homem, seu peso ideial será {ph} Kg, caso seja mulher, {pm}.")


# #### 15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.

# In[26]:


val = float(input("Quanto você ganha por hora trabalhada: "))
horas = 160


# #####  Calcule o salário bruto (horas * salario por hora)

# In[27]:


sal = val * horas


# ##### Calcule o desconto do IR (11% do salário bruto)

# In[28]:


ir = sal * 0.11


# ##### Calcule o desconto do INSS (8% do salário bruto)

# In[29]:


inss = sal * 0.08


# ##### Calcule o desconto do sindicato (5% do salário bruto)

# In[30]:


sind = sal * 0.05


# ##### Calcule o salário líquido (salário bruto - descontos)

# In[31]:


desc = ir + inss + sind

liq = sal - desc

print(f"O seu salário líquido é de {liq}")


# #### 16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R\$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. (para simplificação nesse momento, não se preocupe em arredondar a quantidade de latas a serem compradas - vamos trabalhar isso em breve)

# In[36]:


l = float(input("Informe a largura: "))
c = float(input("Informe o comprimento: "))

a = l * c
clitros = a / 3
latas = clitros / 18
valor = latas * 80.00

print(f"Seram gastas {latas} latas, com um custo total de {valor}.")


# #### 18. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
# 
# Detalhe: MB significa megabyte, Mb (com b minúsculo) significa megabit. Um megabit é 1/8 de um megabyte. 

# In[38]:


tam = float(input("Digite o tamanho do arquivo em Mb: "))
vel = float(input("Digite a velocidade e, Mbps: "))

tempo = tam / vel

print(f"O tempo aproximando para o donwload é de {tempo} s.")

