from bs4 import BeautifulSoup
import requests
import json
import re


def get_data():
    url="https://www.lgl.bayern.de/gesundheit/infektionsschutz/infektionskrankheiten_a_z/coronavirus/karte_coronavirus/index.htm"

    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "html5lib")
    lk_table = soup.find("table", attrs={"id": "tableLandkreise"})
    lk_table_data = lk_table.tbody.find_all("tr")

    headings = []
    for th in lk_table_data[0].find_all("th"):

        headings.append(th.text)


    data_raw = []
    for tr in lk_table_data[1:]:
        row = []
        for td in tr.find_all("td"):
            row.append(td.text.replace('\n', ' ').strip())
        data_raw.append(row)
    return [headings, data_raw]

def json_out():
    data = {"data": []}
    for lk in get_data()[1]:
        tmp = {}
        tmp["name"] = lk[0]
        tmp["cases"] = int(lk[1].replace('.',''))
        if lk[2] == "-":
            tmp["cases_diff"] = 0
        else:
            tmp["cases_diff"] = int(re.sub("[^0-9]", "", lk[2]))
        tmp["case_100k"] = float(lk[3].replace('.','').replace(',','.'))
        tmp["case_7d"] = int(lk[4].replace('.',''))
        tmp["case_7d_100k"] = float(lk[5].replace('.','').replace(',','.'))
        tmp["deaths"] = int(lk[6].replace('.',''))
        if lk[7] == "-":
            tmp["deaths_diff"] = 0
        else:
            tmp["deaths_diff"] = int(re.sub("[^0-9]", "", lk[7]))

        data["data"].append(tmp)
    return json.dumps(data)





