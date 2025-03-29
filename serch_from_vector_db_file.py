import search_client

# Function for display search from  vector DataBase file
def display_search_result(file_name):
    try:
        print("Search result for the request: Do you have BBC news?")
        results = search_client.similarity_search(file_name)
        
        # Printing the results
        for result in results:
            print(result.page_content)
    except Exception:
        print(f"Error display search result from vector database file. No Results")        
    print()