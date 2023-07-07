import requests
from bs4 import BeautifulSoup
from pprint import pprint

def speechresults(url):
    #scrape INVITE page for RESULTS page url
    results=requests.get(url)
    src = results.content
    #html for INVITE page
    soup=BeautifulSoup(src, 'html.parser')
    links=soup.find_all("a")
    for link in links:
        if "Results" in link.text:
            resultspagelink=link.attrs['href']
            if "tourn_id" in resultspagelink:
                resultspagelinkreal=resultspagelink
    #resultspagelinkreal is the url extension for RESULTS page


    #scrape RESULTS page for FINAL PLACES tab
    results=requests.get(f"https://www.tabroom.com/"+resultspagelinkreal)
    src=results.content
    soup=BeautifulSoup(src, 'html.parser')
    links=soup.find_all("a")
    for link in links:
        if "Final Places" in link.text:
            #finalresultslink is link to FINAL PLACES page
            finalplaceslink=link.attrs['href']
    
    #scrape FINAL PLACES page 
    results=requests.get(f"https://tabroom.com/"+finalplaceslink)
    src=results.content
    soup=BeautifulSoup(src, 'html.parser')

    


    speechresults("https://www.tabroom.com/index/tourn/index.mhtml?tourn_id=24562")