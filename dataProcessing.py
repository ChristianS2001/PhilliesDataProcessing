from bs4 import BeautifulSoup #we use bs4 to parse the data (if this is reporting a warning make sure your enviorments are holding the same path for bs4)
import bs4 as bs
import urllib.request #for the link
from dataclasses import dataclass

def main():
    #when we test offline use source from file not weblink
    source = urllib.request.urlopen('https://questionnaire-148920.appspot.com/swe/data.html').read() #we get the link
    #source = open("philliesDataWebPage.html", "r").read() #turns into string
    soup = bs.BeautifulSoup(source,'html.parser') #how we set the html and it is saved into a string

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

    #created the list of players that holds their parsed data such as names, salary, year, level
    playersList = []

    #loop to put player objects with all parameters into a list of players
    for i in range(len(playerNames)):
        playersList.append(players(playerNames[i], playerSalaries[i], playerYears[i], playerLevels[i]))

    #method that turns a list of string salaries into a list of integer salaries and removes key characters + puts a '-1' for when a salaries was corrupted/or empty
    def salStringsToInts(listOfSal): #turning the list of salaries into a list of int salaries
            resultList = []
            for sal in listOfSal:
                if(sal == ""): #edge case for corrupted data #1
                    sal = -1
                
                if(sal != -1 and sal != "no salary data"): #edge case for corrupted data #2
                    sal = sal.strip("$")
                    sal = sal.replace(",","")
                    sal = int(sal)
                else: #clearing all further edge cases
                    sal = -1
                resultList.append(sal)
            return resultList

    salaryList= []
    for i in range(len(playersList)): #fill up salaryList
        salaryList.append(playersList[i].salary)
    
    intSalaryList = salStringsToInts(salaryList) #calling this method on the list of salary strings to create list of salary int's
    for i in range(len(playersList)):
        playersList[i].salary = intSalaryList[i] #filling playersList salaries with correct integer data for future use

    #method to take a list of int(salaries) and return a sorted version greatest->least
    def findTop125Salaries(intSalaryList):
        topSalaries = [] #setting a new list to contain top salaries
        count = 0 #this is to help us figure out when we have reached 125 salaries in topSalaries
        intSalaryList.sort() #sort the list in ascending order
        intSalaryList.reverse() #reverse the sorted list so the highest salaries are first
        for salary in intSalaryList:
            if(count == 125):
                return topSalaries
            else:
                topSalaries.append(salary)
                count+=1

    topSalaries = findTop125Salaries(intSalaryList) #we call findTop125Salaries to create and set a variable to a list of top 125 salaries

    #method to calculate the qualifying salary
    def calculateQualifyingSal(topSalaries):
        qualOfferPrice = 0
        sum = 0
        #calculate qualifying offer price
        for sal in topSalaries:
            if(sal != -1): #this is to make sure we aren't calculating our -1 error check into our qualOfferPrice
                sum += sal
        qualOfferPrice = (sum/125) #math to find the average
        return qualOfferPrice

    finalResult = calculateQualifyingSal(topSalaries) #this is your actual variable that holds the correct float data of the qualifying offer price

    #find a way to print result out to stdout with proper formatting (included correct decimals)
    finalResult = str(finalResult) #turn into string
    qualifyingOfferPrice = "" #create new string to build
    checkStr = "" #create new string to build just the 2 decimal #'s
    decFlag = 0 #flag to see if we passed a '.' char
    for c in finalResult: #loop to get rid of extra decimals
        if(decFlag == 0):
            qualifyingOfferPrice += c
        if(decFlag == 1):
            checkStr += c
        if(c == '.'):
            decFlag = 1
        if(len(checkStr) == 2):
            qualifyingOfferPrice += checkStr

    if(len(checkStr) == 1): #extra check to make sure we put a zero if there is only one decimal present
        qualifyingOfferPrice += checkStr
        qualifyingOfferPrice += "0"

    #here we print qualifyingOfferPrice which is a string version of finalResult, we do this to present the price with the appropiate decimals
    print("The price for the upcoming qualifying offer is:", qualifyingOfferPrice)

if __name__ == "__main__": #running our main
    main()
    '''
        we parse data with "no salary data" , "multiple $$$", no ','s
        and empty string values for salary correctly
    '''
    