# Function to summarize content
import requests
#import create_openip_client
import summarize_content_client
import identify_topics_client
from bs4 import BeautifulSoup

# def scrape_article(url):
#     try:
#         # Send an HTTP request to get the page content
#         response = requests.get(url)
#         response.raise_for_status()  # Check for HTTP request errors
#         soup = BeautifulSoup(response.content, 'html.parser')
        
#         # Extract headline
#         headline = soup.find('h2').get_text(strip=True)
        
#         # Extract full text (basic selector example)
#         paragraphs = soup.find_all('p') 
#         content = ' '.join([para.get_text(strip=True) for para in paragraphs])
        
#         return {"headline": headline, "content": content}
#     except Exception as e:
#         print(f"Error scraping {url}: {e}")
#         return None

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
        # create OpenIP client
        #client = create_openip_client.create_openip_client()

        counter = 0 #temp solution for test
        # Loop through each h2 and find the first following p tag
        for h2 in h2_tags:
            h2_text = h2.get_text(strip=True)  # Get the text content of the h2 tag
            next_p = h2.find_next('p')  # Find the next <p> tag following the h2 tag

            # Get the text content of the paragraph tag, if it exists
            if next_p:
                p_text = next_p.get_text(strip=True)
                p_sammary = summarize_content_client.summarize_content(p_text)
                p_topics = identify_topics_client.identify_topics(p_sammary)
            else:
                p_text = "(No <p> tag following this <h2>)"
                p_sammary = "(No sammary due to there is no <p> tag following this <h2>)"
                p_topics = "(No topics due to there is no <p> tag following this <h2>)"

            # Create a dictionary for JSON
            item = {
                "headline": h2_text,
                "content": p_text,
                "sammary": p_sammary,
                "topics": p_topics
            }

            # Add the object to the list
            results.append(item)
            counter+=1 #temp solution for test
            if counter >= 2: #temp solution for test
                break        
    else:
        print(f"Failed to fetch the webpage. Status code: {response.status_code}")
    return results





