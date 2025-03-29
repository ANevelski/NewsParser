
# Function to find article by Id
def get_item_by_id(articles, item_id):
    for article in articles:
        if article["id"] == item_id:
            return article
    return None

# Function to add summary and topics to article
def add_summarize_and_topics(summary_topics, articles):
    if summary_topics:
        for item in summary_topics:
            id = item["id"]
            article = get_item_by_id(articles, id)
            if article:
                article["summary"] = item["summary"]
                article["topics"] = item["topics"]
    else:
        for article in articles:
            article["summary"] = "No summary"
            article["topics"] = []

    return articles


