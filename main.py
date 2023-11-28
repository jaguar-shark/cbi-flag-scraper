import time
import requests
from bs4 import BeautifulSoup

# API request to community boating to get flag color
cbi_URL = "https://api.community-boating.org/api/flag"


# Function for calling Community Boating Inc. API and returning the flag color
def flagCheck(tries, url):
    for i in range(tries):
        try:
            # Receive content of URL and store color character
            # cbi_URL example content: var FLAG_COLOR = "G"
            page = requests.get(url)
            string = str(BeautifulSoup(page.content, "html.parser"))
            flagColor = string[18]
            # Check which color code the API provides and assign it a full color word string
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


def main():
    print("\nIntializing CBI Flag Check: \n")
    while True:
        print("Checking flag status for CBI...")
        print("Flag color is: " + flagCheck(5, cbi_URL))
        time.sleep(5)


if __name__ == "__main__":
    main()
