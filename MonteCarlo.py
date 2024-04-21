import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ast

class MonteCarlo:
    def __init__(self, df):
        self.__df = df

    def getDf(self):
        return self.__df
    
    def setDf(self, df):
        self.__df = df
    
    def userPorOrg(self, df):
        orgs = df['organization_id']
        users = df['user']
        org_u = set(orgs)
        dic_userPorOrg = {}

        dic_userPorOrg = self.montaDictUser(df, org_u, dic_userPorOrg)
        
        return self.montaDf(dic_userPorOrg, user=True, path=False)

    def montaDictUser(self, df, org_u, dic_userPorOrg):
        for i,org in enumerate(org_u):
            df_aux = df.loc[(df["organization_id"] == org),:]
            user_aux = df_aux["user"]
            dic_userPorOrg[org] = len(set(user_aux))
        return dic_userPorOrg
    
    def montaDf(self, dic, user, path):
        organizations = []
        lista_aux = []
        for k,v in dic.items():
            organizations.append(k)
            lista_aux.append(v)

        if user:
            df_userPorOrg = self.montaDfUserPorOrg(organizations=organizations, n_users=lista_aux)
            return df_userPorOrg
        elif path:
            df_pathPorOrg = self.montaDfPathPorOrg(organizations=organizations, paths=lista_aux)
            return df_pathPorOrg
    
    def montaDfUserPorOrg(self, organizations, n_users):
        df_userPorOrg = pd.DataFrame({
            'organization_id': organizations,
            'N_users': n_users
        })

        df_userPorOrg = df_userPorOrg.sort_values(ascending=False, by='N_users').reset_index(drop=True)

        return df_userPorOrg
    
    def pathPorOrg(self, df):
        dic_pathPorOrg = {}
        paths_list_t = []
        df_userPorOrg = self.userPorOrg(df=df)
        orgs = df_userPorOrg["organization_id"]

        dic_pathPorOrg, paths_list_t = self.montaDictPath_pathsT(df, dic_pathPorOrg, paths_list_t, orgs)

        df_paths = self.montaDfPath(paths_list_t)
        
        return self.montaDf(dic_pathPorOrg, user=False, path=True), df_paths, paths_list_t

    def montaDfPath(self, paths_list_t):
        df_paths = pd.DataFrame()
        df_paths['Count'] = pd.Series(paths_list_t).value_counts().values
        df_paths['Actions'] = pd.Series(paths_list_t).value_counts().keys()
        return df_paths

    def montaDictPath_pathsT(self, df, dic_pathPorOrg, paths_list_t, orgs):
        for org in orgs:
            path_aux = df.loc[(df["organization_id"] == org),(["path_actions"])]
            paths_list_u = []
            lista = [ast.literal_eval(paths[0]) for paths in path_aux.values]
            paths_list_u.extend((set(lista[0]))) #extend adiciona cada elemento da lista em paths_list
            paths_list_t.extend((lista[0])) #extend adiciona cada elemento da lista em paths_list_u
            dic_pathPorOrg[org] = (set(paths_list_u))
        return dic_pathPorOrg, paths_list_t
    
    def montaDfPathPorOrg(self, organizations, paths):
        df_pathPorOrg = pd.DataFrame({
            'organization_id': organizations,
            'Paths': paths
        })

        return df_pathPorOrg
    
    def fazExcel(self, df):
        df.to_excel('Possibiladades.xlsx')

    def plot(self, df):
        plt.figure(figsize=(10,7))

        _, df_paths, paths_list_t = self.pathPorOrg(df)

        plt.subplot(1,3,1)
        plt.bar(df_paths['Actions'], df_paths['Count'], edgecolor='black', linewidth=1.2, alpha=0.7)
        plt.xticks(rotation=90)
        plt.title('Contagem Actions - Bar')

        plt.subplot(1,3,2)
        plt.hist(paths_list_t, edgecolor='black', linewidth=1.2, alpha=0.7)
        plt.xticks(rotation=90)
        plt.title('Contagem Actions - Hist')

        plt.subplot(1,3,3)
        plt.boxplot(df_paths['Count'])
        plt.title('Contagem Actions - Box')
        plt.show()
    
    def run(self):
        self.fazExcel(self.pathPorOrg(self.__df)[0])
        self.plot(self.__df)

    
