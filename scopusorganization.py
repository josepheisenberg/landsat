import pandas
import numpy 

dfa = pandas.read_csv("scopusretrievaldataa.csv")
dfb = pandas.read_csv("scopusretrievaldatab.csv")
dfc = pandas.read_csv("scopusretrievaldatac.csv")
dfd = pandas.read_csv("scopusretrievaldatad.csv")
dfe = pandas.read_csv("scopusretrievaldatae.csv")

wholeframe = [dfa, dfb, dfc, dfd, dfe]

finaldf = pandas.concat(wholeframe)

finaldf.to_csv("ScopusRetrievalDataFinal.csv")