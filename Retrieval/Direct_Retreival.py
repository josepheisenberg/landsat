import requests
from bs4 import BeautifulSoup
import pandas
import re
import numpy
df = pandas.read_csv('ScopusRetrievalDataFinal.csv')
data = []
error_eids = []
eids=df["9"].iloc[[i for i in range(29900,30164)]]
eids = eids.tolist()
for i in range(len(eids)):
    eids[i] = eids[i].strip()
api_key='5b386aef8dc900fb95cdc303bd422586'
for eid in eids:
    url = 'https://api.elsevier.com/content/abstract/eid/'+eid+'?apiKey='+api_key
    response = requests.get(url)
    try:
        if(response.status_code == 200):
            soup = BeautifulSoup(response.content, 'xml')
            try:
                doi = soup.find('doi').get_text()   
            except:
                doi = ""
                pass
            try:
                description = soup.find('description').get_text()
            except:
                description  =""
                pass
            try:
                abstract = soup.find('abstract').get_text()        
            except:
                abstract = ""
                pass
            try:
                affil = soup.find('affiliation')
                affil_pattern = re.compile("id=\"(\d+)\"")
                affil_id = (affil_pattern.search(str(affil))).group(1)
            except:
                affil_id = ""
                pass
            try:
                affil_name = soup.find("affilname").get_text()
            except:
                affil_name = ""
                pass
            try:
                affil_city = soup.find("affiliation-city").get_text()
            except:
                affil_city = ""
                pass
            try:
                affil_country = soup.find("affiliation-country").get_text()
            except:
                affil_country = ""
                pass
            try:
                agg_type = soup.find('aggregationType').get_text() 
            except:
                agg_type = ""
                pass
            try:
                title = soup.find('title').get_text()
            except:
                title = ""
                pass
            try:
                open_access = soup.find("openaccessFlag").get_text()
            except:
                open_access = ""
                pass
            try:
                cite_count = soup.find('citedby-count').get_text()
            except:
                cite_count = ""
                pass
            try:
                au_keywords = []
                au_kw = soup.find('authkeywords').find_all('author-keyword')
                for word in au_kw:
                    au_keywords.append(word.text)
            except:
                au_keywords = ""
                pass
            try:
                idx_keywords = []
                idx_kw = soup.find('idxterms').find_all('mainterm')
                for word in idx_kw:
                    idx_keywords.append(word.text)
            except:
                idx_keywords = ""
                pass
            try:
                auth_nm = soup.find('authors').find_all('indexed-name')
                author_names = []
                for word in auth_nm:
                    author_names.append(word.get_text())
                author_names = list(set(author_names))
            except:
                auth_nm = ""
                pass

            data.append([title, [affil_id, affil_name, affil_city, affil_country], cite_count, agg_type, au_keywords, idx_keywords, abstract, description, doi, eid, open_access])
        else:
            error_eids.append(eid)
    except:
        error_eids.append(eid)
        pass
df_data = pandas.DataFrame((data))
df_data.columns = ['Title', "Affiliation", "Cited By Count", "Aggregation Type", "Author Keywords", "Index Keywords", "Abstract", "Description", "DOI", "eid", "Open Access?"]
df_data.to_csv("scopusretrievalnewe.csv", index = False)
df_err = pandas.DataFrame(numpy.array(error_eids))
df_err.columns = ['Error Eids']
df_err.to_csv("scopusretrievalerroreidse.csv", index = False)
print(len(data))
print(error_eids)