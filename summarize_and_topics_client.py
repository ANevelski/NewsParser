import json

# Function to summarize content
# Returs JSON {"id": "article id ", "summary" : "summary text", "topics": ["topics array"]}  
def summarize_and_get_topics_content(client, content):
    try:      
        # Get data with summary and topics in JSON format   
        # response = client.chat.completions.create(
        #     response_format={ "type": "json_object" },
        #     messages=[
        #         {"role": "system", "content": "You are a helpful assistant summarizing articles and get topics designed to output JSON."},                
        #         {"role": "user", "content": f"Summarize the following article in less than 7 words:  and Extract 2-3 main keywords or topics relating to this article:{content} \n"
        #              '{\n'
        #              '"summary": "string",\n'
        #              '"topics": "array",\n'                
        #             '}'  
        #         }
        #     ],
        #     max_tokens=4096,
        #     temperature=1.0,
        #     top_p=1.0,
        #     model="gpt-4o"
        # )

        response = client.chat.completions.create(
            response_format={ "type": "json_object" },
            messages=[
                {"role": "system", "content": "You are a helpful assistant summarizing articles and extracting topics designed to output JSON objects containing 'summary' and 'topics'."},                
                {"role": "user", "content": f"Here are multiple JSON objects. For each object, generate a summary in less than 7 words and extract 2-3 main keywords or topics:\n\n{content}"}
            ],
            max_tokens=4096,
            temperature=1.0,
            top_p=1.0,
            model="gpt-4o"
        )

        result = json.loads(response.choices[0].message.content)
        return result["results"]
    except Exception as e:
        print(f"Error during summarization and topics retrieving: {e}")
        return None