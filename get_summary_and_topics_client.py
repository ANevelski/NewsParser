import summarize_and_topics_client
import create_openip_client

# Function to parce news from site
def summarize_and_topics_for_articals(articles):
    # Looping through a list of objects (JSON array) to add summary and topics
    articles_content = []
    for article in articles:          
        articles_content.append({ "id": article["id"], "article": article['content']})
        
    client = create_openip_client.create_openip_client()   
      
    # Returs JSON {"id": "article id ", "summary" : "summary text", "topics": ["topics array"]}  
    summarys_topics = summarize_and_topics_client.summarize_and_get_topics_content(client, articles_content)        
        
    return summarys_topics
            
