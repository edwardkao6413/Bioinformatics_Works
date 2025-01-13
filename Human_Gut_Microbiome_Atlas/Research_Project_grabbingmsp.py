#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
pd.set_option('display.max_columns', 50)
pd.set_option('display.max_rows', 50)
import requests
from bs4 import BeautifulSoup
import random


# In[49]:


user_agent_list=[
            'Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0)',
            'Mozilla/4.0(compatible;MSIE8.0;WindowsNT6.0;Trident/4.0)',
            'Mozilla/4.0(compatible;MSIE7.0;WindowsNT6.0)',
            'Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11',
            'Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
            'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36',  
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
        ]

data = pd.read_csv("vect_atlas.csv")
taxa_id = list(data['Unnamed: 0'])
taxa_names = []

taxa_df = pd.DataFrame()
taxa_df['id'] = taxa_id
taxa_df['name'] = ['0' for i in range(len(taxa_id))]


# In[47]:


for i in range(0, len(taxa_id)):
    url = 'https://www.microbiomeatlas.org/species.php?species_msp=' + taxa_id[i]
    header = random.choice(user_agent_list)
    response = requests.get(url, headers = {'user-agent':header})
    response_text = response.text
    soup = BeautifulSoup(response_text, 'html')
    try:
        taxa_name = soup.find_all('h1')[1].text
        if taxa_name:
            taxa_df.at[i, 'name'] = taxa_name
    except:
        pass


# In[48]:


taxa_df.to_csv('corresponding_taxa.csv', index = False)


# In[ ]:





# In[ ]:




