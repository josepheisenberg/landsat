import pybliometrics.scopus as scpapi
import numpy
import pandas

df = pandas.read_csv('scopusdata3.csv')
data = []
counter = 0
errors = []
for i in range(40000, len(df["Eids"])):
    counter +=1
    eid = df["Eids"][i]
    try:
        absreq = scpapi.AbstractRetrieval(eid.strip(), id_type = 'eid')
        if(absreq.aggregationType == 'Journal'):
            try:
                data.append([absreq.title, absreq.aggregationType, absreq.authors, absreq.citedby_count, absreq.affiliation, absreq.abstract, absreq.description, absreq.get_bibtex(), absreq.doi, eid])
            except:
                print(absreq.doi)
                errors.append([eid, 1])
                pass
    except:
        errors.append([eid, 0])
        print(eid, "EID")
        pass

print(counter)
df = pandas.DataFrame(numpy.array(data))
df.to_csv("scopusretrievaldatae.csv")
df = pandas.DataFrame(numpy.array(errors))
df.to_csv("scopuserrorse.csv")
    

        
