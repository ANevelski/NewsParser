# Function for displaying results
def print_articles(articles):
    for item in articles:
        print(f"Headline {item['id']+1}: {item['headline']}")
        print(f"Content: {item['content']}")   
        summary_value = item.get("summary")
        if summary_value is not None:    
            print(f"Summary: {summary_value}")  
        else:
            print(f"Summary: {'No summary'}")
        
        topics_value = item.get("topics")
        if topics_value is not None and len(topics_value) > 0: 
            print(f"Topics:")
            counter = 1 
            for topic in topics_value:
                print(f"{counter}. {topic}")
                counter+=1
        else:
            print(f"Topics: {'No topics'}") 
        print("-" * 40)
        print()