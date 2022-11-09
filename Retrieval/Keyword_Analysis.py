import numpy as np
import pandas as pd
import re


df = pd.read_csv("ScopusRetrievalDataNewFinal.csv")
df_array = df.to_numpy()
running_words = list()
doc_rows = []
df_reference = pd.read_csv("C:/CS/ILSResearch/landsat/landsat_abstracts_with_keywordscount.csv")

df_ref_array = df_reference.to_numpy()
#print(df_ref_array[0][3])
#print(df_ref_array[0][9])
title_group_dict = dict()
doi_group_dict = dict()
for i in range(len(df_ref_array)):
    doi_group_dict[df_ref_array[i][6]] = df_ref_array[i][9]
    title_group_dict[df_ref_array[i][3]] = df_ref_array[i][9]
for i in range(len(df_array)):
    keyworda = df_array[i][4]
    keyworda = re.sub("[\]\[\'\']", "", keyworda)
    keywordb = df_array[i][5]
    keywordb = re.sub("[\]\[\'\']", "", keywordb)
    keyworda = keyworda.lower()
    keywordb = keywordb.lower()
    keyworda = keyworda.split(',')
    keywordb = keywordb.split(',')
    keywords=list(set(keyworda).union(set(keywordb)))
    if(keywords.count('') > 0):
       keywords.remove('')
    keywords = [i.strip() for i in keywords]
    if(len(keywords) > 0):
        try:
            doc_rows.append([df_array[i][0], df_array[i][9], list(set(keywords)), int(title_group_dict[df_array[i][0]])])
        except:
            try:
                doc_rows.append([df_array[i][0], df_array[i][9], list(set(keywords)), int(doi_group_dict[df_array[i][8]])])
            except:
                doc_rows.append([df_array[i][0], df_array[i][9], list(set(keywords)), str(i)])
                pass
        for i in keywords:
            running_words.append(i)
for i in range(len(doc_rows)):
    if(type(doc_rows[i][3]) != type(12) and type(doc_rows[i][3]) != type(12.01)):
        if(i < len(doc_rows) - 1):
            if(doc_rows[i-1][3] == doc_rows[i+1][3]):
                doc_rows[i][3] = doc_rows[i-1][3]
            else:
                doc_rows[i][3] = "Not found"
        else:
            doc_rows[i][3] = "Not found"
#print(len(list(set(running_words))))
doc_rows.append(["All keywords", "N/A", list(set(running_words)), "N/A"])
nparr = np.array(doc_rows)
dfout = pd.DataFrame(nparr, columns = ['Title', 'Eid', "Keywords", "Year Group"])
dfout.to_csv("Keywords_Spreadsheet.csv", index = False)