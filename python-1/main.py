# coding: utf-8

# Todas as perguntas são referentes ao arquivo `data.csv`
# Você ** não ** pode utilizar o pandas e nem o numpy para este desafio.

import csv
data = []
with open('pandas-1/data.csv', mode='r') as csvfile:
    csv_reader = csv.reader(csvfile)
    line_count = 0
    for row in csv_reader:
        data.append(row)

header = data[0]
nationality_idx = header.index('nationality')
club_idx = header.index('club')
name_idx = header.index('full_name')
wage_idx = header.index('eur_wage')
age_idx = header.index('age')

# **Q1.** Quantas nacionalidades (coluna `nationality`) diferentes existem no arquivo?
# 
def q_1():
    nationality_col = []
    for row in data[1:]:
        nationality_col.append(row[nationality_idx])
    
    return len(set(nationality_col))

# **Q2.** Quantos clubes (coluna `club`) diferentes existem no arquivo?
def q_2():
    club_col = []
    for row in data[1:]:
        club_col.append(row[club_idx])
    print(len(set(club_col)))
    return (len(set(club_col)))
q_2()

# **Q3.** Liste o primeiro nome dos 20 primeiros jogadores de acordo com a coluna `full_name`.
def q_3():
    names = []
    for row in data[1:21]:
        names.append(row[name_idx])
    return (names)

# **Q4.** Quem são os top 10 jogadores que ganham mais dinheiro (utilize as colunas `full_name` e `eur_wage`)?
def q_4():
    names = []
    sorted_wages = sorted(data[1:],key=lambda x: float(x[wage_idx]), reverse=True) 
    for row in sorted_wages[:10]:
        names.append(row[name_idx])
    return (names)

# **Q5.** Quem são os 10 jogadores mais velhos?
def q_5():
    names = []
    sorted_ages = sorted(data[1:], key=lambda x: x[age_idx], reverse=True)
    for row in sorted_ages[:10]:
        names.append(row[name_idx])
    print(names)
    return (names)
#q_5()

# **Q6.** Conte quantos jogadores existem por idade. Para isso, construa um dicionário onde as chaves são as idades e os valores a contagem.
def q_6():
    age_count = {}

    for row in data[1:]:
        if int(row[age_idx]) in age_count:
            age_count[int(row[age_idx])] += 1
        else: 
            age_count[int(row[age_idx])] = 1
    return age_count

