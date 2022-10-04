# PhilliesDataProcessing
 This is for the Phillies SWE Internship/Associate position

 We need to process the top 125 salaries in the team, then take that average and set that as the qualifying offer for a departing free agent player

When a team signs a free agent they give up a draft pick.

We use this data set: https://questionnaire-148920.appspot.com/swe/data.html

The data changes slightly each time you reload the page this is ensuring the code is dynamic and properly parses the data new and old.

Display any other relevant data the the user regarding finding that qualifying offer price: (EX: names?, highest current salary?, USD(currency)?, etc..)

There will be data without certain fields or corrupted or malformed names. Ignore missing values but make sure they don't effect the average. 

Make sure code is readable, presented nicely, and use comments to describe your functionality.

Also make sure to add a ReadME.md to explain how to get the results I get.

Step #1: Make sure to install BeautifulSoup via typing "pip install BeautifulSoup4" on your terminal line
Issue: This was incredibly finiky for me due to me installing python via windows shop, this is good for using VSCode however it causes issues with the library being used globally which caused certain errors for me.

Step #2: 
