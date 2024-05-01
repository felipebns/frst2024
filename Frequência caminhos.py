import pandas as pd

user_paths_df = pd.read_csv(r"C:\Users\thoma\Downloads\dados_brutos.csv", sep=";", index_col=0)
all_paths_df = pd.read_csv(r"C:\Users\thoma\Desktop\INSPER\Entidades\Data\FRST\out.csv", sep=";", index_col=0)

merged_df = pd.merge(user_paths_df, all_paths_df, left_on="path_actions", right_on="path")

path_frequency = merged_df["path_name"].value_counts()

#print(path_frequency)


total_count = path_frequency.sum()

path_frequency = (path_frequency/total_count)
path_frequency = pd.merge(path_frequency, all_paths_df[['path_name', 'path']], on='path_name')
 
print(path_frequency)
