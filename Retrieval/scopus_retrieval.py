import pybliometrics.scopus as scpapi
import numpy
import pandas

df = pandas.read_csv('ScopusRetrievalDataFinal.csv')
finddata = df.to_numpy()
data = []
counter = 0
errors = []
for i in range(1):
    counter +=1
    eid = finddata[i][11]
    #print(eid)
    #try:
    absreq = scpapi.AbstractRetrieval(eid.strip())
    print(absreq)
    if(absreq.aggregationType == 'Journal'):
            #try:
        data.append([absreq.title, absreq.aggregationType, absreq.authors, absreq.citedby_count, absreq.affiliation, absreq.authkeywords, absreq.abstract, absreq.description, absreq.doi, eid])
        #print(absreq.authkeywords)
            #except:
                #print(absreq.doi)
                #errors.append([eid, 1])
                #pass
    #except:
     #   errors.append([eid, 0])
      #  print(eid, "EID")
       # pass

#print(counter)
df = pandas.DataFrame(numpy.array(data))
df.to_csv("scopusretrievaldatatesting.csv")
df = pandas.DataFrame(numpy.array(errors))
df.to_csv("scopuserrortestingerr.csv")
    

        
