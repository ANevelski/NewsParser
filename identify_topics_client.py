import create_openip_client

# Function to identify topics
def identify_topics(content):
    try:       
        client = create_openip_client.create_openip_client()

        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a topic extraction expert."},
                {"role": "user", "content": f"Extract 2-5 main topics or keywords relating to this article: {content}"}
            ],
            max_tokens=4096,
            temperature=1.0,
            top_p=1.0,
            model="gpt-4o"
        )
       
        topics = response.choices[0].message.content

        return topics
    except Exception as e:
        print(f"Error during topic identification: {e}")
        return None