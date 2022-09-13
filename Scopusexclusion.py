import pandas
import time

df = pandas.read_csv("ScopusRetrievalDataFinal.csv")

data = df.values
exclude = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(len(data))
for i in data:
    flag = True
    for j in exclude:
        if(flag):
            if(i[j] == None):
                data.pop(data.index(i))
                flag = False
print(len(data))