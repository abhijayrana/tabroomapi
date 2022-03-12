from bs4 import BeautifulSoup
import requests
from pprint import pprint

result=requests.get(f"https://www.tabroom.com/index/tourn/results/event_results.mhtml?tourn_id=20648&result_id=191603")
src=result.content
soup=BeautifulSoup(src, "html.parser")

try:
    tablebreaks = soup.find("table", id="191603-1")
    rows = tablebreaks.select("tr")

    speechbreakstats=[]

    for row in rows[1:]:
        _, place, _, entry, _, school, _, score, *rest = row.children
        place = place.string.strip()
        entry = entry.string.strip()
        school = school.string.strip()
        score= score.string.strip()

        if school=="Bellarmine College Prep":
            tempstorage=(place, entry, school, score)
            speechbreakstats.append(tempstorage)
except AttributeError:
    pass

pprint(speechbreakstats)

try:
    tableprelims = soup.find("table", id="191603-2")
    rows = tableprelims.select("tr")

    speechprelimsstats=[]

    for row in rows[1:]:
        _, place, _, entry, _, school, _, score, *rest = row.children
        place = place.string.strip()
        entry = entry.string.strip()
        school = school.string.strip()
        score= score.string.strip()

        if school=="Bellarmine College Prep":
            tempstorage=(place, entry, school, score)
            speechprelimsstats.append(tempstorage)
except AttributeError:
    pass

pprint(speechprelimsstats)