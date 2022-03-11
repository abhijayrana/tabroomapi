from bs4 import BeautifulSoup
from pprint import pprint
import requests

#get all tournament links from CFL homepage
alltournaments=[]

def getournament():
    result=requests.get("https://www.tabroom.com/index/circuit/calendar.mhtml?circuit_id=67")
    src=result.content
    soup=BeautifulSoup(src, 'html.parser')
    table=soup.find('table')
    tablelinks=table.find_all("a")
    print(soup.prettify())
    for link in tablelinks:
        if "CFL" in link.text:
            tournamentappend=(link.text, link.attrs['href'])
            alltournaments.append(tournamentappend)
    print(alltournaments)


def fib(n):
    print(n)