import os
import scrape_articles_client
import get_summary_and_topics_client
import add_summary_and_topics_to_articles
import display_articals_client
import serch_from_vector_db_file
import vector_store_client

# Get news site from settings
url = os.getenv("NEWS_SITE_URL")

# Get news from site
articles = scrape_articles_client.scrape_article(url)

# Get summary and topics
summarys_topics = get_summary_and_topics_client.summarize_and_topics_for_articals(articles)

# Add summary and topics to articles
articles = add_summary_and_topics_to_articles.add_summarize_and_topics(summarys_topics, articles)

# Display result
display_articals_client.print_articles(articles)

# Saving to vector database file
file_name = vector_store_client.save_to_vector_database_file(articles)

# Perform search from vector DataBase file and display result (relevantes summary)
serch_from_vector_db_file.display_search_result(file_name)