from ast import arguments
from curses import raw
from optparse import Values
from readline import redisplay
from turtle import right
import requests
from bs4 import BeautifulSoup
from pprint import pprint
from readdata import fib, getournament


varr='hello'
fib(varr)

alltournamentslinks=getournament()

#SUPERDEBATE 1

sd1=[]
for tournament in alltournamentslinks:
    
    (text, linkgg)=tournament

    if "Super Debate" in text:

        linkggg=linkgg

        #scrapes data from tournament homepage, specifically it scrapes the results tab url
        result=requests.get(f"https://www.tabroom.com"+linkgg)
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

        #scrapes results page, navigating to the 'Final Places' tab
        result=requests.get(f"https://www.tabroom.com/"+resultfinal)
        src=result.content
        soup=BeautifulSoup(src, 'html.parser')
        #print(soup.prettify())
        links=soup.find_all("a")
        finalresultslink=""
        for link in links:
            if "Final Places" in link.text:
                finalresultslink=link.attrs['href']
                #print(finalresultslink)

        #scrapes initial final places tab and finds tournament id, round id, and number of rounds.
        finalresult=requests.get(f"https://www.tabroom.com"+finalresultslink)
        src=result.content
        soup=BeautifulSoup(src, 'html.parser')

        items=soup.select('option[value]')
        values=[item.get('value') for item in items]
        eventlength=len(values)
        roundidnew=finalresultslink[-6:]
        #print(roundidnew)
        roundidnew=int(roundidnew)
        tableids0=[roundidnew]
        roundidnew=int(roundidnew)
        for value in values:
            roundidnew=roundidnew+1
            tableids0.append(roundidnew)
        tableids0.pop()
        #print(tableids0)

        #tableids0 is the list of all table ids

        #extracts tournamentid from tournament id link (VERY SKETCHY CODE)
        tournamentid=finalresultslink[-22:]
        tournamentid=tournamentid[0:5]
        #print(tournamentid)

        #get data for all competitors in specified tournament (specified by tourn id)
        #currently filtering only bellarmine students and currently only displaying win number, names, school

        for tablenumber in tableids0:
            table_id = tablenumber

            #uses tournament id and event id to scrape individual pages from a tournament
            params = {"tourn_id": tournamentid, "result_id": table_id}
            result = requests.get(f"https://www.tabroom.com/index/tourn/results/event_results.mhtml", params=params)
            src = result.content
            #print(src)
            # with open("tabroom.html", "r") as f:
            #     src = f.read()

            soup = BeautifulSoup(src, 'html.parser')
            #print(soup.prettify())


            #links=soup.find_all("select")
            #print(links)
            #print("\n")

            #items=soup.select('option[value]')
            #values=[item.get('value') for item in items]
            #print(values)
            #print(items)

            #scrapes names, schools, and results from table
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
                        entry=entry.replace('AP ','')
                    # print(f"{place} | {entry} | {school} | {winpm}")
                        tempstorage=(place, entry, school, winpm)
                        bellstats.append(tempstorage)

                #print(bellstats)
                for stat in bellstats:
                    sd1.append(stat)
            except AttributeError:
                pass
        print(linkggg)
    
#    if "Speech" in text and "State" not in text:




#results sorted by win number
print('------------DEBATE RESULTS-------------')
def getkey(item):
    return item[3]
sd1.sort(key=getkey)
pprint(sd1)
