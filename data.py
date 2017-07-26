from bs4 import BeautifulSoup
import requests
import csv
url = "http://solarrooftop.gov.in/getmnreKML"
r = requests.get(url)

soup = BeautifulSoup(r.text,"html.parser")

descriptions = soup.find_all("description")

with open("data.csv","w+") as f:
    writer = csv.writer(f)
    writer.writerow(["Customer Code","Capacity in KW","State","District","Latitude","Longitude","Total Cost (Rs)","CFA (Rs)","Commissioning Date(installation date)","Approval Number","Financial Year","Installed by Agency"])
    for description in descriptions:
        table_rows = BeautifulSoup(description.text,"html.parser").find_all("tr")
        customer_code = table_rows[2].find_all("td")[-1].text.strip()
        capacity = table_rows[3].find_all("td")[-1].text.strip()
        state = table_rows[4].find_all("td")[-1].text.strip()
        district = table_rows[5].find_all("td")[-1].text.strip()
        lat = table_rows[6].find_all("td")[-1].text.strip()
        lon = table_rows[7].find_all("td")[-1].text.strip()
        total_cost = table_rows[8].find_all("td")[-1].text.strip()
        cfa = table_rows[9].find_all("td")[-1].text.strip()
        commisioning = table_rows[10].find_all("td")[-1].text.strip()
        approval = table_rows[11].find_all("td")[-1].text.strip()
        financial = table_rows[12].find_all("td")[-1].text.strip()
        installed = table_rows[13].find_all("td")[-1].text.strip()
        writer.writerow([customer_code,capacity,state,district,lat,lon,total_cost,cfa,commisioning,approval,financial,installed])
