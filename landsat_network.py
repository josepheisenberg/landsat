import pandas as pd
import numpy
import networkx as nx
import pyvis
from pyvis.network import Network

landsat_net = Network(height="1000px", width="100%", font_color="black",heading='2022-1975 Landsat Article Keyword Overlap')
df = pd.read_csv('network_connections.csv')
graph = nx.Graph()
count = -1
dictio = {"forest" : 1, "urban" : 1, "water": 1, "crop" : 1, "glacier" : 1, "water quality" : 2, "carbon" : 2, "ecosystem" : 2, "climate change" : 2, "soil erosion" : 2, "surface temperature" : 2, "ecosystem service" : 2, "urban expansion" : 2, "habitat" : 2, "biomass" : 2, "google earth engine" : 3, "time series" : 3, "object based image" : 3, "machine learning" : 3, "neural network" : 3, "support vector machine" : 3, "random forest" : 3, "change detection" : 3, "land use land cover" : 4, "normalized difference vegetation index": 4, "land surface temperature": 4, "normalized difference water index": 4, "digital elevation model": 4, "normalized difference built index" : 4, "leaf area index" : 4}
for i in df.columns:
    if(count >= 0 and i != "gis" and i != "climate"):
        numvals = df.values[count][count+1]
        size = 5*numpy.log(numvals) + numvals * .02
        graph.add_node(i, label = i, size = size * .3, title = i, group = dictio[i])
    count += 1
for i in range(1, len(df.values)):
    for j in range(i+1, len(df.values[i])):
        if(df.values[i-1][j] > 180 and df.columns[i] != "gis" and df.columns[i] != "climate" and df.columns[j] != "gis" and df.columns[j] != "climate"):
            w = .025  * (df.values[i-1][j])
            graph.add_edge(df.columns[i], df.columns[j], width = w)
landsat_net.from_nx(graph)
landsat_net.barnes_hut(gravity=-2000, central_gravity=0.3, spring_length=50, spring_strength=0.001, damping=0.09, overlap=0)
landsat_net.show("landsatnetwork.html") 