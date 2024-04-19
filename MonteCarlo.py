import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ast

class MonteCarlo:
    def __init__(self, df):
        self.df = df

    def getDf(self):
        return self.df
    
    def setDf(self, df):
        self.df = df
    
    def userPorOrg(self, df):
        orgs = df['organization_id']
        users = df['user']
        org_u = set(orgs)
        dic_userPorOrg = {}
        for i,org in enumerate(org_u):
            df_aux = df.loc[(df["organization_id"] == org),:]
            user_aux = df_aux["user"]
            dic_userPorOrg[org] = len(set(user_aux))
        
        return self.montaDfUserPorOrg(dic_userPorOrg)
    
    def montaDfUserPorOrg(self, dic):
        organizations = []
        n_users = []
        for k,v in dic.items():
            organizations.append(k)
            n_users.append(v)

        df_userPorOrg = pd.DataFrame({
            'organization_id': organizations,
            'N_users': n_users
        })

        df_userPorOrg = df_userPorOrg.sort_values(ascending=False, by='N_users').reset_index(drop=True)

        return df_userPorOrg
    
    def pathPorOrg(self, df):
        dic_pathPorOrg = {}
        df_userPorOrg = self.userPorOrg(df=df)
        orgs = df_userPorOrg.head(20)["organization_id"]

        for org in orgs:
            path_aux = df.loc[(df["organization_id"] == org),(["path_actions"])]
            paths_list = []
            lista = [ast.literal_eval(paths[0]) for paths in path_aux.values]
            paths_list.extend((set(lista[0]))) #extend adiciona cada elemento da lista em paths_list
            dic_pathPorOrg[org] = (set(paths_list))
        
        return self.montaDfPathPorOrg(dic_pathPorOrg)
    
    def montaDfPathPorOrg(self, dic):
        organizations2 = []
        paths = []
        for k,v in dic.items():
            organizations2.append(k)
            paths.append(v)

        df_pathPorOrg = pd.DataFrame({
            'organization_id': organizations2,
            'Paths': paths
        })

        return df_pathPorOrg
    
    def fazExcel(self, df):
        df.to_excel('Possibiladades.xlsx')
    
    def run(self):
        self.fazExcel(self.pathPorOrg(self.df))

    
