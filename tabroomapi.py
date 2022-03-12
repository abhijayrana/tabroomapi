from ast import arguments
from curses import raw
from optparse import Values
from readline import redisplay
from turtle import right
import requests
from bs4 import BeautifulSoup
from pprint import pprint
from readdata import fib, getournament
from debateevents import getdebateresults


varr='hello'
fib(varr)

alltournamentslinks=getournament()

#SUPERDEBATE 1

sd1=[]
for tournament in alltournamentslinks:
    
    (text, linkgg)=tournament

    #non quals debate events
    if "Super Debate" in text:
        linkggg=linkgg
        getdebateresults(linkgg, sd1)
        print(linkggg)
    
    #if "Speech" in text and "State" not in text:




#debate esults sorted by win number
print('------------DEBATE RESULTS-------------')
def getkey(item):
    return item[3]
sd1.sort(key=getkey)
pprint(sd1)
