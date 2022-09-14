import pandas as pd
import numpy
import networkx as nx
import pyvis
from pyvis.network import Network

landsat_net = Network(height="1000px", width="100%", font_color="black",heading='Landsat term overlap')
df = pd.read_csv('network_connections.csv')
graph = nx.Graph()
count = -1
for i in df.columns:
    if(count >= 0):
        numvals = df.values[count][count+1]
        size = 5*numpy.log(numvals) + numvals * .02 - 20
        graph.add_node(i, size = size, title = i)
    count += 1
for i in range(len(df.values)):
    for j in range(i+1, len(df.values[i])):
        w = numpy.log(df.values[i-1][j])
        graph.add_edge(df.columns[i], df.columns[j], width = w)
        print(df.columns[i], df.columns[j], df.values[i-1][j])
landsat_net.from_nx(graph) 
landsat_net.show("landsatnet.html") 