import create_openip_client

# Function to summarize content
def summarize_content(content):
    try:        
        client = create_openip_client.create_openip_client()

        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful assistant summarizing articles."},
                {"role": "user", "content": f"Summarize the following article in less than 10 words: {content}"}
            ],
            max_tokens=4096,
            temperature=1.0,
            top_p=1.0,
            model="gpt-4o"
        )
  
        summary = response.choices[0].message.content
        return summary
    except Exception as e:
        print(f"Error during summarization: {e}")
        return None