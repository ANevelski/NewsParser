import json

# Function to summarize content
# Returs JSON {"summary" : "summary text", "topics": ["topics array"]}
def summarize_and_get_topics_content(client, content):
    try:      
        # Get data with summary and topics in JSON format   
        response = client.chat.completions.create(
            response_format={ "type": "json_object" },
            messages=[
                {"role": "system", "content": "You are a helpful assistant summarizing articles and get topics designed to output JSON."},                
                {"role": "user", "content": f"Summarize the following article in less than 7 words:  and Extract 2-3 main keywords or topics relating to this article:{content} \n"
                     '{\n'
                     '"summary": "string",\n'
                     '"topics": "array",\n'                
                    '}'  
                }
            ],
            max_tokens=4096,
            temperature=1.0,
            top_p=1.0,
            model="gpt-4o"
        )  
        result = json.loads(response.choices[0].message.content)
        return result
    except Exception as e:
        print(f"Error during summarization and topics retrieving: {e}")
        return None