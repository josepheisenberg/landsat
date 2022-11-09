import pandas
import numpy 

dfb = pandas.read_csv("scopusretrievalnewb.csv")
dfc = pandas.read_csv("scopusretrievalnewc.csv")
dfd = pandas.read_csv("scopusretrievalnewd.csv")
dfe = pandas.read_csv("scopusretrievalnewe.csv")

wholeframe = [dfb, dfc, dfd, dfe]

finaldf = pandas.concat(wholeframe)

#arr = finaldf.to_numpy()

finaldf.to_csv("ScopusRetrievalDataNewFinal.csv", index = False)