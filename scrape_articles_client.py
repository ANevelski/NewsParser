import requests
from bs4 import BeautifulSoup

# Function to get nes from site
def scrape_article(url):
    # Send an HTTP request to fetch the HTML content of the page
    response = requests.get(url)

    # Ensure the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all h2 tags
        h2_tags = soup.find_all('h2')

        # List to store JSON objects
        results = []

        # counter = 0 #temp solution for test
        # Loop through each h2 and find the first following p tag
        for h2 in h2_tags:
            h2_text = h2.get_text(strip=True)  # Get the text content of the h2 tag
            next_p = h2.find_next('p')  # Find the next <p> tag following the h2 tag

            # Get the text content of the paragraph tag, if it exists
            if next_p:
                p_text = next_p.get_text(strip=True)                
            else:
                p_text = ""               

            # Create a dictionary for JSON
            item = {
                "headline": h2_text,
                "content": p_text
            }

            # Add the object to the list
            results.append(item)
            # counter+=1 #temp solution for test
            # if counter >= 1: #temp solution for test
            #     break
    else:
        print(f"Failed to fetch the webpage. Status code: {response.status_code}")
    return results





