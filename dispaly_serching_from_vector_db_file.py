import search_client

# Function for display search from  vector DataBase file
def do_search(file_name):
    print("Search result for the request: Do you have BBC news?")
    results = search_client.similarity_search(file_name)
    
     # Printing the results
    for result in results:
        print(result.page_content)
    print()