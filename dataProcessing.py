from bs4 import BeautifulSoup #we use bs4 to parse the data (if this is reporting a warning make sure your enviorments are holding the same path for bs4)
import bs4 as bs
import urllib.request #for the link
from dataclasses import dataclass

def main():
    #when we test offline use source from file not weblink
    #source = urllib.request.urlopen('https://questionnaire-148920.appspot.com/swe/data.html').read() #we get the link
    source = open("philliesDataWebPage.html", "r").read() #turns into string
    soup = bs.BeautifulSoup(source,'html.parser') #how we set the html and it is saved into a string
    
    #we are creating count variables to make sure we don't ruin our calculations from our parsing function
    countOfPlayers = 0
    countOfSalaries = 0

    #function here to parse soup so that we can extract the data
    def parseNames(data):
        playerNames = []
        for parseData in data.find_all("td", {'class':'player-name'}):
            playerNames.append(parseData.get_text())
        return playerNames

    def parseSalary(data):
        playerSalaries = []
        for parseData in data.find_all("td", {'class':'player-salary'}):
            playerSalaries.append(parseData.get_text())
        return playerSalaries

    def parseYear(data):
        playerYears = [] #these seem like they will all be "2016"
        for parseData in data.find_all("td", {'class':'player-year'}):
            playerYears.append(parseData.get_text())
        return playerYears

    def parseLevel(data):
        playerLevels = [] #these seem like they will all be "MLB"
        for parseData in data.find_all("td", {'class':'player-level'}):
            playerLevels.append(parseData.get_text())
        return playerLevels

    @dataclass
    class players: #data class so we can make a list of it
        name: str
        salary: str
        year: str
        level: str
        def __str__(self):
            return "%s, %s, %s, %s"%(self.name, self.salary, self.year, self.level) #formatting the string for future printing

    #calling these methods with soup (our html parser) these are returning lists
    playerNames = parseNames(soup)
    playerSalaries = parseSalary(soup)
    playerYears = parseYear(soup)
    playerLevels = parseLevel(soup)

    playersList = []

    #loop to put things into a list of players
    for i in range(len(playerNames)):
        playersList.append(players(playerNames[i], playerSalaries[i], playerYears[i], playerLevels[i]))

    '''for player in playersList: TESTING!!!
        print(player)'''

    #print(playersList[0].name) #can print the name of whatever player in the list per index you can also do .salary , .year, .level

if __name__ == "__main__": #running our main
    main()