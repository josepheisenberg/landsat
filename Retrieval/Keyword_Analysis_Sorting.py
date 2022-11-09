import pandas as pd
import numpy as np

df = pd.read_csv("Keywords_By_Yeargroup_unsorted.csv")
df_array = df.to_numpy()
list_years = []
for i in range(10):
    list_years.append([])
    for j in df_array:
        list_years[i].append([j[2*i+1], j[2*i]])
    list_years[i] = sorted(list_years[i], reverse = True)
expanded_list_years = []
for i in list_years:
    expanded_list_years.append([])
    expanded_list_years.append([])
for j in range(len(df_array)):
    for i in range(len(list_years)):
        expanded_list_years[2*i].append(list_years[i][j][1])
        expanded_list_years[2*i+1].append(list_years[i][j][0])
out_data = np.array(expanded_list_years)
dfout = pd.DataFrame(np.transpose(out_data), columns = ['2022 words', "2022 counts", '2020 words', "2020 counts", "2019 words", "2019 counts", "2018 words", "2018 counts", "2017 words", "2017 counts", "2015 words", "2015 counts", "2012 words", "2012 counts", "2008 words", "2008 counts", "1997 words", "1997 counts", "1985 words", "1985 counts"])
dfout.to_csv("Keywords_By_Yeargroup_sorted.csv", index = False)