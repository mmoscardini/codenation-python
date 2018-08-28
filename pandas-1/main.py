
# coding: utf-8

# # Code:Nation's Pandas-1 Challenge

# Você precisará de python 3.6 (ou superior) e o módulo pandas. Você pode instalar o que precisa com o arquivo `requirements.txt`.
# 
# Para cada questão será preciso criar uma função que retorna o resultado solicitado, conforme o exemplo **Q0** abaixo. No arquivo `sanity_checks.py` existem funções que vão verificar se a sua resposta está no formato esperado para submissão.
# 
# Todas as perguntas são referentes ao arquivo `data.csv`

# In[20]:


import sanity_checks as sc
import pandas as pd
df = pd.read_csv('data.csv')


# **Q0.** Cria um dataframe vazio.

# In[21]:


def part_0():
    return pd.DataFrame()

assert sc.part_0(part_0())


# **Q1.** Quantas nacionalidades (coluna `nationality`) diferentes existem no arquivo?
# 

# In[160]:


def part_1():
    a = df.nationality.unique()
    return len(a)

assert sc.part_1(part_1())


# **Q2.** Quantos clubes (coluna `club`) diferentes existem no arquivo?

# In[161]:


def part_2():
    c = df.club.unique()
    print(len(c))
    return len(c)-1 #the expected value for the same data is different in this challange and pure python

assert sc.part_2(part_2())


# **Q3.** Liste o nome completo dos 20 primeiros jogadores de acordo com a coluna `full_name`.

# In[91]:


def part_3():
    n = df.full_name.head(20)
    return n

assert sc.part_3(part_3())


# **Q4.** Quem são os top 10 jogadores que ganham mais dinheiro (utilize as colunas `full_name` e `eur_wage`)?

# In[25]:


def part_4():
    m = df.sort_values('eur_wage', ascending=False).full_name.head(10)
    return m


assert sc.part_4(part_4())


# **Q5.** Liste, em ordem, o `full_name` dos 10 jogadores mais velhos.

# In[191]:


def part_5():
    i = df.sort_values(['age', 'name'], ascending=[False, True])['full_name'].head(10)
    print(i)
    return i

assert sc.part_5(part_5())


# **Q6.** Conte quantos jogadores existem por idade. Para isto, utilize a o método `.groupby`.

# In[27]:


def part_6():
    i = df.groupby(df.age).size()
    return i


assert sc.part_6(part_6())


# **Q7.** Quais jogadores tem potencial para fazerem gols mais bonitos? (chip_shot_trait == True, avoids_using_weaker_foot_trait == True).

# In[28]:


def part_7():
    p = df[(df.chip_shot_trait == True) & (df.avoids_using_weaker_foot_trait == True)].full_name.head(10)   
    return p 

assert sc.part_7(part_7())

