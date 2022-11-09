import numpy as np
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords

df = pd.read_csv("ScopusRetrievalDataNewFinal.csv")
df_reference = pd.read_csv("C:/CS/ILSResearch/landsat/landsat_abstracts_with_keywordscount.csv")

df_ref_array = df_reference.to_numpy()
df_array = df.to_numpy()
abstracts = []
title_group_dict = dict()
doi_group_dict = dict()
for i in range(len(df_ref_array)):
    doi_group_dict[df_ref_array[i][6]] = df_ref_array[i][9]
    title_group_dict[df_ref_array[i][3]] = df_ref_array[i][9]
for i in range(len(df_array)):
    abstract = df_array[i][6]
    if(type(abstract) == type("Words")):
        abstract = re.sub(r'[^\w ]', '', abstract)
        abstract = abstract.lower()
        abstract = abstract.split(" ")
        abstract = [word for word in abstract if word not in stopwords.words('english')]
        while(abstract.count(" ") > 0):
            abstract.remove(" ")
        while(abstract.count("") > 0):
            abstract.remove("")
        try:
            abstracts.append([df_array[i][0], df_array[i][9], abstract, int(title_group_dict[df_array[i][0]])])
        except:
            try:
                abstracts.append([df_array[i][0], df_array[i][9], abstract, int(doi_group_dict[df_array[i][8]])])
            except:
                abstracts.append([df_array[i][0], df_array[i][9], abstract, str(i)])
                pass
for i in range(len(abstracts)):
    if(type(abstracts[i][3]) != type(12) and type(abstracts[i][3]) != type(12.01)):
        if(abstracts[i-1][3] == abstracts[i+1][3] and i < len(abstracts) - 1):
            abstracts[i][3] = abstracts[i-1][3]
        else:
            abstracts[i][3] = "Not found"

nparr = np.array(abstracts)
dfout = pd.DataFrame(nparr, columns = ['Title', 'Eid', "Abstracts", "Year Group"])
dfout.to_csv("Abstract_Spreadsheet.csv", index = False)