#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd


data = {'Nom' : ['John', 'Mary', 'Bob', 'Sarah', 'Tom', 'Lisa'],
        'Département' : ['IT', 'Marketing', 'Sales', 'IT', 'Finance', 'Marketing'], 
        'Âge' : [30, 40, 25, 35, 45, 28], 
        'Sexe' : ['Homme', 'Femme', 'Homme', 'Femme ', 'Homme', 'Femme'], 
        'Salaire' : [50000, 60000, 45000, 55000, 70000, 55000], 
        'Expérience' : [3, 7, 2, 5, 10, 4]}


# In[15]:


df = pd.DataFrame(data)


# In[16]:


print(df)


# In[44]:


#1. Selectionner les trois premieres lignes de la trames de donnnes
df.iloc[0:3]


# In[49]:


#2.Utilisez la méthode loc pour sélectionner toutes les lignes où le département est « Marketing ».
df.loc[df["Département"]=='Marketing']


# In[58]:


#3.Utilisez la méthode iloc pour sélectionner les colonnes Âge et Sexe pour les 4 premières lignes du dataframe.
df.iloc[0:4,2:4]


# In[73]:


#4.Utilisez la méthode loc pour sélectionner les colonnes Salaire et Expérience pour toutes les lignes où le sexe est « Homme ».
df.loc[df["Sexe"]=='Homme',['Salaire','Expérience']]


# In[ ]:




