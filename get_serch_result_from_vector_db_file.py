import os
import search_client

# Function do search in vector DataBase file
def do_search(file_name, search_question):
    try:        
        documents = search_client.similarity_search(file_name, search_question)        
        return documents        
    except Exception:
        print(f"Error during search result from vector database file by user question.")        
        return None

# Function to find article's headlines related to search result in vector DataBase file
def find_artical_by_search_results(documents_search_results, articles):
    try:
        article_headlines = []
        if documents_search_results:
            # Printing the results
            for document in documents_search_results:
                # Search for the first article object
                article = next((article for article in articles if article["summary"] == document.page_content), None)
                if article:
                    article_headlines.append(article["headline"])
        return article_headlines
    except Exception:
        print(f"Error during find  search article by summary.")        
        return None


# Function for display search from  vector DataBase file
def display_search_result(file_name, articles):
    try:
        # Display user's question request
        search_question = os.getenv("USER_QUESTION_FOR_SEARCH")
        print(f"Search result for the request: '{search_question}'")

        # Retrive related articles headlines by user's question request
        documents_search_results = do_search(file_name, search_question)
        related_articles_headlines = find_artical_by_search_results(documents_search_results, articles)
        
        # Display search result
        if related_articles_headlines is not None and len(related_articles_headlines) > 0:
            for headline in related_articles_headlines:
                print(headline)
        else:
            print("Related articles were not found.")
    except Exception:  
        print(f"Error display article search result by user question in article's summaries.") 
    print()