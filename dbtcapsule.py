import requests
from bs4 import BeautifulSoup
from pprint import pprint

#works for pf, ld, parli, cx?

def debateresults(url):
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


    dropdownlist = soup.find("select")
    options = dropdownlist.select("option")
    eventsattourney = len(options)

    for x in range(eventsattourney):

        #scrape FINAL PLACES page 
        results=requests.get(f"https://tabroom.com/"+finalplaceslink)
        src=results.content
        soup=BeautifulSoup(src, 'html.parser')

        #scrapes table
        try:    

            #finds table_id/round_id from url
            table_id=finalplaceslink[-6:]
            #finds correct table
            table=soup.find('table', id=f"{table_id}-1")
            rows=table.select("tr")

            #scrape table header to find categories
            categoryrow=rows[0]
            categories=[]
            categories=categoryrow.select("th")

            #filter categories list 
            categoriesList=[]
            for category in categories:
                categoryvar = category.string.strip()
                if categoryvar != "Ballots":
                    categoriesList.append(categoryvar)
            #pprint(categoriesList)


            allcompetitordata = []

            #scrape table by row and category
            for row in rows[1:]:
                columns = row.find_all('td')
                competitordata={}
                if columns!=[]:
                    for category in categoriesList:
                        #print(category)
                        column=categoriesList.index(category)
                        #pprint(column)
                        data=columns[column].string.strip()

                        competitordata[category] = data
                    
                    #pprint(competitordata)

                allcompetitordata.append(competitordata)
            
            pprint("DATA ONG ___________-")
            pprint(allcompetitordata)

            newtableid = int(table_id)
            newtableid = newtableid + 1 
            newtableid = str(newtableid)
            finalplaceslink = finalplaceslink[:-6] + newtableid

        except AttributeError:
            pass





    




debateresults("https://www.tabroom.com/index/tourn/index.mhtml?tourn_id=24551")