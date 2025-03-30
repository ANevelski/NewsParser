import requests
from bs4 import BeautifulSoup

# Function to remove article's duplicates
def remove_duplicates(articles):
    # Comparison based on only certain fields ("headline" and "content")
    seen = set()
    unique_articles = []
    for article in articles:
        # Create a unique key based on the specified fields
        key = (article["headline"], article["content"])  # Compare only equate the fields "headline" and "content"
        if key not in seen:
            seen.add(key)
            unique_articles.append(article)
    return unique_articles

# Function to adding Id to each article
def add_id_to_articles(articles):    
    counter = 1    
    for article in articles:
        article["id"] = counter
        counter += 1
    return articles

# Function to get news articles from site
def scrape_articles(url):
    # Send an HTTP request to fetch the HTML content of the page
    response = requests.get(url)

    # Ensure the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all h2 tags
        h2_tags = soup.find_all('h2')

        # List to store JSON objects
        articles = []

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
            article = {                
                "headline": h2_text,
                "content": p_text
            }

            # Add the object to the list
            articles.append(article)
    else:
        print(f"Failed to fetch the webpage. Status code: {response.status_code}")
    
    # Exclude not news items
    articles = [article for article in articles if "Copyright" not in article.get("content", "")]
    
    # Eliminate duplicates
    articles = remove_duplicates(articles)

    # Add Id to articles
    articles = add_id_to_articles(articles)

    return articles





