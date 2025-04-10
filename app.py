import os
import asyncio
import scrape_articles_client
import get_summary_and_topics_client
import add_summary_and_topics_to_articles
import display_articals_client
import get_serch_result_from_vector_db_file
import vector_store_client

import demonstration_of_article_with_long_context 

# Get news site from settings
url = os.getenv("NEWS_SITE_URL")

# Get news from site
articles = scrape_articles_client.scrape_articles(url)

# Get summary and topics
summarys_topics = get_summary_and_topics_client.summarize_and_topics_for_articals(articles)

# Add summary and topics to articles
articles = add_summary_and_topics_to_articles.add_summarize_and_topics(summarys_topics, articles)

# run demonstration long content with chunking
demonstration_article = asyncio.run(demonstration_of_article_with_long_context.get_result_for_long_content_aticle())

# Merge article lists
articles += demonstration_article

# Display result
display_articals_client.print_articles(articles)

# Saving to vector database file
file_name = vector_store_client.save_to_vector_database_file(articles)

# Perform search from vector DataBase file and display result (relevantes summary)
get_serch_result_from_vector_db_file.display_search_result(file_name, articles)