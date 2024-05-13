import pandas as pd
import ast
import numpy as np

user_paths_df = pd.read_csv(r"C:\Users\thoma\Downloads\dados_brutos.csv", sep=";", index_col=0)
all_paths_df = pd.read_csv(r"C:\Users\thoma\Desktop\INSPER\Entidades\Data\FRST\out.csv", sep=";", index_col=0)

merged_df = pd.merge(user_paths_df, all_paths_df, left_on="path_actions", right_on="path")

path_frequency = merged_df["path_name"].value_counts()

total_count = path_frequency.sum()

path_frequencys = (path_frequency/total_count)
path_frequency = pd.merge(path_frequencys, all_paths_df[['path_name', 'path']], on='path_name')

#algorítmo para visualização dos caminhos

def split_paths(row):
    paths = ast.literal_eval(row['path'])  
    return pd.DataFrame({'path_name': row['path_name'],
                         'count': row['count'],
                         'from_state': paths[:-1],
                         'to_state': paths[1:]})

prob_stat = pd.concat([split_paths(row) for _, row in path_frequency.iterrows()], ignore_index=True)

print (prob_stat)

num = 1000
results = []

def monte_carlo (data):
    return np.random.choice(data['path_name'], p = data['count'])

for _ in range (num):
    simulated_path = monte_carlo(path_frequency)
    results.append(simulated_path)
    
result_count = pd.Series(results).value_counts(normalize = True)
