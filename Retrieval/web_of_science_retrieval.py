from wos import WosClient
import wos.utils
import numpy
import pandas
import regex 


with WosClient() as client:
    data = (wos.utils.query(client, "(TS=(landsat)) AND (DT==(\"ARTICLE\"))"))
print(type(data))
print(regex.findall("pub_info sortdate", data))
#data=numpy.asarray([data])
#df = pandas.DataFrame(data)
#df.to_csv("wosdata.csv")