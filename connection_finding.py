import pandas as pd
import numpy
import networkx as nx
import pyvis


df = pd.read_csv('landsat_abstracts_with_keywordscount.csv')
data = df.values
count = 0
connections = [[0 for i in range(13, 45)] for j in range(13, 45)]
names = [df.columns[i] for i in range(13, 45)]
for i in data:
    specdata = [i[j] for j in range(13, 45)]
    for k in range(len(connections)):
        for l in range(len(connections[k])):
            if(specdata[k] != 0 and specdata[l] != 0):
                connections[k][l] += 1
final_df = pd.DataFrame(numpy.array(connections))
final_df.columns = names
final_df.to_csv("network_connections.csv")        
    
        