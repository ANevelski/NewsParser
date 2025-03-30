import json

# Function to summarize content
# Returs JSON {"id": "article id", "summary" : "summary text", "topics": "[topics array]""}  
def summarize_and_get_topics_content(client, content):
    try:      
        response = client.chat.completions.create(
            response_format={ "type": "json_object" },
            # List of messages for the interaction context
            messages=[
                # Sets the initial instructions for the model (rules and context).
                {"role": "system", "content": "You are a helpful assistant summarizing articles and extracting topics designed to output JSON objects containing 'id', 'summary' and 'topics'."},                
                # A message from a user representing a request or question.
                {"role": "user", "content": f"Here are multiple JSON objects. For each object, add 'id', generate a 'summary' in less than 7 words and extract 2-3 main 'keywords' or 'topics': {content}.Response JSON format:\n"
                  '{"results": "array of JSON object" }\n'
                  'Each JSON object in result format: \n'
                    '{\n'
                            '"id": "int",\n'
                            '"summary": "string",\n'
                            '"topics": "array",\n'                
                    '}'
                }
            ],
            # 
            max_tokens=4096, # Limits the maximum number of tokens in the generated response. The total number of tokens (incoming messages + generated tokens) must not exceed the limit for the selected model.
            temperature=1.0, # Controls the degree of "creativity" of the answer. Range of values: from 0 to 2.
            top_p=1.0, # Alternative to temperature. This parameter limits the selection of tokens to a certain probability percentile (also called "nucleus sampling"). Range: 0 to 1.
            model="gpt-4o" # 
        )

        result = json.loads(response.choices[0].message.content)

        return result["results"]
    except Exception as e:
        print(f"Error during summarization and topics retrieving: {e}")
        return None