from bs4 import BeautifulSoup #we use bs4 to parse the data (if this is reporting a warning make sure your enviorments are holding the same path for bs4)
import bs4 as bs
import urllib.request #for the link

def main():
    source = urllib.request.urlopen('https://questionnaire-148920.appspot.com/swe/data.html').read() #we get the link
    soup = bs.BeautifulSoup(source,'html.parser') #how we set the html and it is saved into a string
    #print(soup) #this print is proving that we are now pulling the data properly!
    
    #we are creating count variables to make sure we don't ruin our calculations from our parsing function
    countOfPlayers = 0
    countOfSalaries = 0

    #we create a list of player objects to store data
    playersList = []

    #testing section
    '''
    playersList.append( player("Jerry Springs", "$1,000,000", 2016, "MLB")) #test for list
    print("name: " + playersList[0].name, "salary: " + playersList[0].salary, "year: " + str(playersList[0].year), 
        "level: "+ playersList[0].level, sep=', ')
    '''

    #function here to parse soup so that we can extract the data
    def parseData(data):
        #data may ACTUALLY be a list! look into it
        #data is going to be soup in this case but the functionality will work with any input stream
        newString = ""
        for c in data: #loop per character in soup
            newString += c
            #if(data[i] == 'n' and data[i+1] == 'a' and data[i+2] == 'm' and data[i+3] == 'e'):
                #do something to save name data
        print(newString)

    parseData(soup) #calling parseData with soup
            


                






class player:
    def __init__(self, name, salary, year, level):
        #this is a function that will hold data for a player
        self.name = name #ex Soria, Joakim
        self.salary = salary #ex $7,000,000
        self.year = year #2016
        self.level = level #ex MLB

if __name__ == "__main__": #running our main
    main()