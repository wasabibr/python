#!/usr/bin/env python
# coding: utf-8

# ### F-string

# In[1]:


faturamento = 1000
custo = 400

lucro = faturamento - custo

# com format
print("O faturamento foi de {} e o lucro de {}".format(faturamento, lucro))

# com f-string
print(f"O faturamento foi de {faturamento} e o lucro de {faturamento - custo}")


# ### Mudança de tipo de variável

# In[2]:


faturamento = float(input("Insira o faturamento"))
custo = float(input("Insira o custo"))

print(type(faturamento))
print(type(custo))

lucro = faturamento - custo

print(lucro)

# str -> muda para string
# int -> muda para inteiro
# float -> muda para float

