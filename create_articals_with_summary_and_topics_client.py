import summarize_and_topics_client
import create_openip_client

# Function to parce news from site
def summarize_and_topics_for_artical(articles):
    # Looping through a list of objects (JSON array) to add summary and topics
    client = create_openip_client.create_openip_client()
    for article in articles:  
        # Returs JSON {"summary" : "summary text", "topics": ["topics array"]}  
        summary_topics = summarize_and_topics_client.summarize_and_get_topics_content(client, article['content'])        
        article["summary"] = summary_topics["summary"]    
        article["topics"] = summary_topics["topics"]
            
