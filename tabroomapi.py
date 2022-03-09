from ast import arguments
from optparse import Values
from readline import redisplay
from turtle import right
import requests
from bs4 import BeautifulSoup

table_id = 189553

params = {"tourn_id": 20646, "result_id": table_id}
result = requests.get(f"https://www.tabroom.com/index/tourn/results/event_results.mhtml", params=params)
# print(result.status_code)
#print(result.headers)

src = result.content
#print(src)
# with open("tabroom.html", "r") as f:
#     src = f.read()

soup = BeautifulSoup(src, 'html.parser')
#print(soup.prettify())


links=soup.find_all("select")
#print(links)
#print("\n")

items=soup.select('option[value]')
values=[item.get('value') for item in items]
#print(values)
#print(items)

# for item in items:
#     #print(item.attrs)
#     try:
#         print(item['selected'])  
#         print(item['value'])
#     except:
#         print('didnt work')
    # if hasattr(item, 'selected'):
    #     print(item['selected'])
    # else:
    #     print('no select')




# for link in links:
#    if "Final" in link.text:
#         print(link)
#         print(link.attrs['href'])

table = soup.find("table", id=f"{table_id}-1")
rows = table.select("tr")

bellstats=[]

for row in rows[1:]:
    _, place, _, entry, _, school, _, winpm, *rest = row.children
    place = place.string.strip()
    entry = entry.string.strip()
    school = school.string.strip()
    winpm = winpm.string.strip()
    if school=="Bellarmine College Prep":
        entry=entry.replace('BelCol','')
       # print(f"{place} | {entry} | {school} | {winpm}")
        tempstorage=(place, entry, school, winpm)
        bellstats.append(tempstorage)

print(bellstats)


