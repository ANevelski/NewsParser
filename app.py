import os
import scrape_articles_client
import vector_store_client
import search_client

url = os.getenv("NEWS_SITE_URL")
articles = scrape_articles_client.scrape_article(url)

file_name = vector_store_client.save_to_vector_database(articles)

# Looping through a list of objects (JSON array)
for item in articles:
    print(f"Headline: {item['headline']}")
    print(f"Content: {item['content']}") 
    print(f"Sammary: {item['sammary']}")
    print(f"Topics:")
    print(f"{item['topics']}")
    print("-" * 40)
    print()

print("Search result for the request: Do you have BBC news?")
search_client.similarity_search(file_name)
