import pybliometrics.scopus as scpapi
import numpy
import pandas

df = pandas.read_csv('ScopusRetrievalDataFinal.csv')
data = []
counter = 0
errors = []
for i in range(100):
    counter +=1
    eid = df["9"][i]
    print(eid.strip())