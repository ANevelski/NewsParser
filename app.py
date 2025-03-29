import os
import scrape_articles_client
import vector_store_client
import create_articals_with_summary_and_topics_client
import print_articals_client
import dispaly_serching_from_vector_db_file

# Get news site from settings
url = os.getenv("NEWS_SITE_URL")

# Get news from site
articles = scrape_articles_client.scrape_article(url)

# Add summary and topics
create_articals_with_summary_and_topics_client.summarize_and_topics_for_artical(articles)

#Display result
print_articals_client.print_articles(articles)

# Saving to vector database file
file_name = vector_store_client.save_to_vector_database(articles)

#Perform search from vector DataBase file and display result (relevantes summary)
dispaly_serching_from_vector_db_file.do_search(file_name)
