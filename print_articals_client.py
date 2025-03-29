# Function for displaying results
def print_articles(articles):
    for item in articles:
        print(f"Headline: {item['headline']}")
        print(f"Content: {item['content']}")       
        print(f"Sammary: {item['summary']}")                
        print(f"Topics:")
        counter = 1 
        for topic in item['topics']:
            print(f"{counter}. {topic}")
            counter+=1
        print("-" * 40)
        print()