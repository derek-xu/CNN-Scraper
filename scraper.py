import requests
from bs4 import BeautifulSoup

# URL of the website you want to scrape
url = 'https://edition.cnn.com/world'  # Replace with the actual URL

# Send a GET request to fetch the webpage
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all <span> elements with the class 'container__headline-text'
    headlines = soup.find_all('span', class_='container__headline-text')
    
    # Print out each headline
    print("Today's Headlines:\n")
    for headline in headlines:
        print(headline.get_text().strip())

else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
