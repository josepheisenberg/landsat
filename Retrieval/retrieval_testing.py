import requests
from bs4 import BeautifulSoup
import pandas
import re
import numpy

df = pandas.read_csv('ScopusRetrievalDataFinal.csv')
eids=df["9"].iloc[[i for i in range(29900,30165)]]
print(eids)

