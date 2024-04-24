import pandas as pd

df=pd.read_excel(r"C:\Users\thoma\Desktop\INSPER\Entidades\Data\FRST\dados_brutos.xlsx")


estados = {}

acess_count = df.groupby('organization_id')['user'].nunique().nlargest(20)      #Contador em grupo dos acessos únicos de usuários das 20 maiores id's de empresa
top20 = df[df['organization_id'].isin(acess_count.index)]       #Filtragem em df do df original apenas das empresas presentes no top20
caminhos = top20.groupby('organization_id')['path'].unique()        #Organização dos caminhos das empresas no top20

#for org_id,paths in caminhos.items():
    print(f"Empresa !!!!!!!!!! {org_id}")
    for path in paths:
        print(path)
    print()
    

