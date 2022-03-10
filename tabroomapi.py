from ast import arguments
from curses import raw
from optparse import Values
from readline import redisplay
from turtle import right
import requests
from bs4 import BeautifulSoup
from pprint import pprint

#SUPERDEBATE 1

sd1=[]

result=requests.get("https://www.tabroom.com/index/tourn/index.mhtml?tourn_id=20646")
src=result.content
soup=BeautifulSoup(src, 'html.parser')
resultslink=""
resultfinal=""
links=soup.find_all("a")
for link in links:
    if "Results" in link.text: 
        resultslink=link.attrs['href']
        if "tourn_id" in resultslink:
            resultfinal=resultslink

result=requests.get(f"https://www.tabroom.com/"+resultfinal)
src=result.content
soup=BeautifulSoup(src, 'html.parser')
#print(soup.prettify())
links=soup.find_all("a")
finalresultslink=""
for link in links:
    if "Final Places" in link.text:
        finalresultslink=link.attrs['href']
        print(finalresultslink)

finalresult=requests.get(f"https://www.tabroom.com"+finalresultslink)
src=result.content
soup=BeautifulSoup(src, 'html.parser')

items=soup.select('option[value]')
values=[item.get('value') for item in items]
eventlength=len(values)
roundidnew=finalresultslink[-6:]
print(roundidnew)
roundidnew=int(roundidnew)
tableids0=[roundidnew]
roundidnew=int(roundidnew)
for value in values:
    roundidnew=roundidnew+1
    tableids0.append(roundidnew)
tableids0.pop()
print(tableids0)

#tableids1=[189552, 189553, 189554, 189555, 189556, 189557, 189558, 189559]

tournamentid=finalresultslink[-22:]
tournamentid=tournamentid[0:5]
print(tournamentid)

for tablenumber in tableids0:
    table_id = tablenumber

    params = {"tourn_id": tournamentid, "result_id": table_id}
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

    try:
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

        #print(bellstats)
        for stat in bellstats:
            sd1.append(stat)
    except AttributeError:
        pass

print('------------SUPERDEBATE 1-------------')
#print(sd1)
def getkey(item):
    return item[3]
sd1.sort(key=getkey)
pprint(sd1)

# #SUPERDEBATE 2

# sd2=[]
# tableids=[198126, 198127, 198128, 198129, 198130, 198131, 198132]

# for tablenumber in tableids:
#     table_id = tablenumber

#     params = {"tourn_id": 20650, "result_id": table_id}
#     result = requests.get(f"https://www.tabroom.com/index/tourn/results/event_results.mhtml", params=params)
#     # print(result.status_code)
#     #print(result.headers)

#     src = result.content
#     #print(src)
#     # with open("tabroom.html", "r") as f:
#     #     src = f.read()

#     soup = BeautifulSoup(src, 'html.parser')
#     #print(soup.prettify())


#     links=soup.find_all("select")
#     #print(links)
#     #print("\n")

#     items=soup.select('option[value]')
#     values=[item.get('value') for item in items]
#     #print(values)
#     #print(items)

#     try:
#         table = soup.find("table", id=f"{table_id}-1")
#         rows = table.select("tr")

#         bellstats=[]

#         for row in rows[1:]:
#             _, place, _, entry, _, school, _, winpm, *rest = row.children
#             place = place.string.strip()
#             entry = entry.string.strip()
#             school = school.string.strip()
#             winpm = winpm.string.strip()
#             if school=="Bellarmine College Prep":
#                 entry=entry.replace('BelCol ','')
#                 entry=entry.replace('AP ', '')


#             # print(f"{place} | {entry} | {school} | {winpm}")
#                 tempstorage=(place, entry, school, winpm)
#                 bellstats.append(tempstorage)

#         #print(bellstats)
#         for stat in bellstats:
#             sd2.append(stat)
#     except AttributeError:
#         pass

# print('------------SUPERDEBATE 2-------------')
# def getkey(item):
#     return item[3]
# sd2.sort(key=getkey)
# #pprint(sd2)