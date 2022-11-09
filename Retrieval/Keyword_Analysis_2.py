import numpy as np
import pandas as pd
import re

df = pd.read_csv("Keywords_Spreadsheet.csv")
df_array = df.to_numpy()

all_keys = df_array[len(df_array)-1][2]
all_keys = all_keys.split(", ")
count_dict_list = []
for i in range(len(all_keys)):
    all_keys[i] = re.sub("[\]\[\'\']", "", all_keys[i])
for i in all_keys:
    count_dict = {2022:0,2020:0,2019:0,2018:0,2017:0,2015:0,2012:0,2008:0,1997:0,1985:0,0:0}
    for j in range(len(df_array)-1):
        keys = df_array[j][2].split(", ")
        for k in range(len(keys)):
            keys[k] = re.sub("[\]\[\'\']", "", keys[k])
        for k in keys:
            if(i == k):
                try:
                    year = int(df_array[j][3])
                except:
                    year = 0
                count_dict[year] += 1
    count_dict_list.append([i, count_dict])
year_list = [2022, 2020, 2019, 2018, 2017, 2015, 2012, 2008, 1997, 1985]
year_list_words = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
for i in year_list:
    for j in count_dict_list:
        year_list_words[year_list.index(i)*2].append(j[0])
        year_list_words[year_list.index(i)*2+1].append(j[1][i])
final_keyword_data = np.array(year_list_words)
dfout = pd.DataFrame(np.transpose(final_keyword_data), columns = ['2022 words', "2022 counts", '2020 words', "2020 counts", "2019 words", "2019 counts", "2018 words", "2018 counts", "2017 words", "2017 counts", "2015 words", "2015 counts", "2012 words", "2012 counts", "2008 words", "2008 counts", "1997 words", "1997 counts", "1985 words", "1985 counts"])
dfout.to_csv("Keywords_By_Yeargroup_unsorted.csv", index = False)
                    
            