import os
import time
import requests
from bs4 import BeautifulSoup

# API request to community boating to get flag color
cbi_URL = "https://api.community-boating.org/api/flag"


# Function for calling CBI api and returning the flag color
def flagCheck(tries, url):
    for i in range(tries):
        try: 
            # Receive content of URL
            page = requests.get(url)
            string = str(BeautifulSoup(page.content, "html.parser"))
            flagColor = string[18]
            if flagColor == "Y":
                    return "Yellow"
            elif flagColor == "R":
                return "Red"
            elif flagColor == "G":
                return "Green"
            else:
                return "Conditions unknown"
        except Exception as error:
            print(error)
            if i < tries - 1:
                continue
            raise
        break
    return flagColor

print(flagCheck(5,cbi_URL))


