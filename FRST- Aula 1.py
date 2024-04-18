import pandas as pd
df = pd.read_csv(r'C:\Users\Arthu\Documents\dados_brutos.csv', sep=';')
df_userPorOrg = df.groupby('organization_id')['user'].nunique().reset_index()
df_userPorOrg.columns = ['organization_id', 'N_users']
df_userPorOrg = df_userPorOrg.sort_values(by='N_users', ascending=False)
top_20_orgs = df_userPorOrg.head(20)
print(top_20_orgs)
