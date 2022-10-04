from bs4 import BeautifulSoup #we use bs4 to parse the data (if this is reporting a warning make sure your enviorments are holding the same path for bs4)
import bs4 as bs
import urllib.request #for the link

def main():
    source = urllib.request.urlopen('https://questionnaire-148920.appspot.com/swe/data.html').read() #we get the link
    soup = bs.BeautifulSoup(source,'html.parser') #how we set the html
    print(soup) #this print is proving that we are now pulling the data properly!
    
    #we are creating count variables to make sure we don't ruin our calculations from our parsing function
    countOfPlayers = 0
    countOfSalaries = 0
    

    




if __name__ == "__main__": #running our main
    main()