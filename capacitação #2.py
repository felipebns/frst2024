import pandas as pd
from ast import literal_eval
import matplotlib.pyplot as plt
import numpy as np

df_dados_brutos = pd.read_csv(r"C:\Users\thoma\Downloads\dados_brutos.csv", sep=";", index_col=0)
df_empresas_selecionadas = pd.read_csv("empresas_selecionadas.csv", sep=";", index_col=0)

empresas_selecionadas = list(set(df_empresas_selecionadas["organization_id"].values))
df_dados_brutos = df_dados_brutos[df_dados_brutos["organization_id"].isin(empresas_selecionadas)]

set(df_dados_brutos['organization_id'].values).difference(empresas_selecionadas)

df_dados_brutos = df_dados_brutos.reset_index(drop=True)
actions = []
for i in range(len(df_dados_brutos)):
    path_actions = df_dados_brutos.at[i,'path_actions']
    if type(path_actions) == str:
        path_actions = literal_eval(path_actions)
    else:
        path_actions = path_actions
    for action in path_actions:
        actions.append(action)

chaves = list(set(actions))
dict_actions = {}
for chave in chaves:
    dict_actions[chave] = 0
    
for action in actions:
    dict_actions[action] += 1
    
#plt.xticks(ticks=range(len(dict_actions.keys())), labels=dict_actions.keys(), rotation=90)
#plt.hist(actions)
#plt.show() 

dict_actions_ordenado = sorted(dict_actions.items(), key=lambda x: x[1], reverse=True)
for chave, valor in dict_actions_ordenado:
    print(chave, valor)
    
#Construção gráfico sem 3 maiores valores    

dict_actions_ordenado1 = dict_actions_ordenado[3:]
valores = [val[1] for val in dict_actions_ordenado1]

media1 = np.mean(valores)
mediana1 = np.median(valores)

plt.bar(range(len(valores)), valores, tick_label=[val[0] for val in dict_actions_ordenado1])
plt.axhline(y=media1, color='b', linestyle='-', label=f'Média sem maiores: {media1:.2f}')
plt.axhline(y=mediana1, color='y', linestyle='-', label=f'Mediana sem maiores: {mediana1}')
plt.xticks(rotation=90)

plt.legend()
plt.show()

#Construção gráfico sem 3 menores valores

dict_actions_ordenado2 = dict_actions_ordenado[:-3]
valores0 = [val[1] for val in dict_actions_ordenado2]

media2 = np.mean(valores0)
mediana2 = np.median(valores0)

plt.bar(range(len(valores0)), valores0, tick_label=[val[0] for val in dict_actions_ordenado2])
plt.axhline(y=media2, color='r', linestyle='-', label=f'Média sem menores: {media2:.2f}')
plt.axhline(y=mediana1, color='g', linestyle='-', label=f'Mediana sem menores: {mediana2}')
plt.xticks(rotation=90)

plt.legend()
plt.show()

#Algorítmo para determinação de assimetria

if media1 > mediana1 and media2 > mediana2:
    print("Assimetria Positiva")
elif media1 < mediana1 and media2 < mediana2:
    print("Assimetria Negativa")
elif media1 > mediana1 and media2 < mediana2:
    print("Assimetria positiva apenas nos valores sem os 3 maiores")
elif media1 < mediana1 and media2 > mediana2:
    print("Assimetria apenas nos valores sem os 3 menores")
else:
    print("Não há determinação de assimetria")