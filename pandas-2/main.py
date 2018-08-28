
# coding: utf-8

# # Code:Nation's Pandas-2 Challenge

# Você precisará de python 3.6 (ou superior) e o módulo pandas. Você pode instalar o que precisa com o arquivo `requirements.txt`.
# 
# Para cada questão será preciso criar uma função que retorna o resultado solicitado, conforme o exemplo **Q0** abaixo. No arquivo `sanity_checks.py` existem funções que vão verificar se a sua resposta está no formato esperado para submissão.
# 
# Todas as perguntas são referentes ao arquivo `data.csv`
# 
# Você **não** pode utilizar o pandas e nem o numpy para este desafio.

# In[90]:


import sanity_checks as sc
import pandas as pd

df = pd.read_csv('data.csv')
df.columns.values


# **Q0.** Cria um dataframe vazio.

# In[3]:


def part_0():
    return pd.DataFrame()

assert sc.part_0(part_0())


# **Q1.** Quais clubes possuem jogadores de pelo menos 15 nacionalidades diferentes?
# 

# In[250]:


def part_1():
    a = df.groupby(['club'])['nationality'].nunique()
    a = a[a > 14].index.to_series()
    return a

assert sc.part_1(part_1())


# **Q2.** Qual a nacionalidade com a média de jogadores mais pesados?

# In[88]:


def part_2():
    b = df.groupby('nationality')['weight_kg'].aggregate('mean').sort_values(ascending=False)
    return b.index[0]

assert sc.part_2(part_2())


# **Q3.** Dos jogadores que tem mais de 1.90 de altura quantos são da Espanha?

# In[125]:


def part_3():
    c = df[df.height_cm > 190].groupby('nationality').size()
    return c[c.index == 'Spain'][0]

assert sc.part_3(part_3())


# **Q4.** Quantos jogadores tem ao menos 3 posições preferidas? Utilize as colunas que iniciam com `prefers_`.

# In[151]:


def part_4():
    d = df.iloc[:, -27:-1]
    d = d.sum(axis=1)
    return len(d[d>=3])

assert sc.part_4(part_4())


# **Q5.** Quantas pessoas pertencem a clubes que possuem jogadores de pelo menos 10 nacionalidades diferentes?

# In[274]:


def part_5():
    e = df.groupby(['club'])['nationality'].nunique()
    e = e[e>9].index
    return len(df.loc[df.club.isin(e)])

assert sc.part_5(part_5())


# In[273]:




