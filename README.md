**Steps on how to get my results**

***Result should something like this***
*The price for the upcoming qualifying offer is: 16544994.14*

Step #1: Make sure to install BeautifulSoup via typing "pip install BeautifulSoup4" on your terminal line
Issue: This was incredibly finiky for me due to me installing python via windows shop, this is good for using VSCode however it causes issues with the library being used globally which caused certain errors for me.

Step #2: Download the dataProcessing.py, philliesDataWebPage.html (if you want to parse from file), and a way to run python code (via IDE or terminal with python installed) or you can download the entire github repo as a zipped folder with the link I provided.

GitHub Repository Link: https://github.com/ChristianS2001/PhilliesDataProcessing

Step #3: Make sure you are either scrapping the info from the webpage or the html file (there is a command present in code to use from file, just uncomment the source = filereader, and comment out the source = bs(html.parser)) |this is done near lines 8 and 9|.

Step #4: This is not really a step more rather me telling you that the finalResult variable is the actual float with qualifying offer price, what is being printed is actually just a formatted string for better presentation. |this is in reference to lines 109 and 131|.

Note: My answer to part A of this coding challening is in this repo as a .txt file

Here is the answer for part A just in case:

A. The code I would use to validate if the string is a palindrome is this:

class Solution(object):
    def isPalindrome(self, s):
        s = ''.join(e for e in s if e.isalnum()).lower() #making it so string s is replacing all non letter char's into nothing then lowercasing the ones that are letter chars
        return s==s[::-1] #[::-1] starts at the end of a string and moves back, this is returning the BOOL of if S from start the finish, and S from finish to start = eachother

This code is an improvement in my opinion because it is shorter and more scalable. We are using library functions from the Python language and on top of that we make use of Python
functionality with the return statement. Since the algorithm will be used or copied and rarely modified for it's task I find a shorter implementation is always better, and a programmer
should always take advantage of a languages functionality. This runtime is also faster, however we do sacrifice space-time complexitiy here since we use .isalnum() and .lower(). If we
wanted to not waste space we would implement a version using a left and right pointer and not build a string to check, rather check the characters themselves.
