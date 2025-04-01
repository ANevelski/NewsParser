import json
import asyncio
from langchain_text_splitters import RecursiveCharacterTextSplitter
import create_openip_client

# Function to summarize long content by CHUNKS
# Return array with demonstration article 
async def sent_request_to_ai(client, chunk):
    try:
        response = client.chat.completions.create(
                response_format={ "type": "json_object" },
                # List of messages for the interaction context
                messages=[
                    # Sets the initial instructions for the model (rules and context).
                    {"role": "system", "content": "You are a helpful assistant summarizing articles and extracting topics designed to output JSON objects containing 'id', 'summary' and 'topics'."},                
                    # A message from a user representing a request or question.
                    {"role": "user", "content": f"Here is an JSON object. Please generate a 'summary' in less than 5 words and extract 2 main 'keywords' or 'topics': {chunk}.:\n"
                    'Response JSON format: \n'
                        '{\n'                            
                                '"summary": "string",\n'
                                '"topics": "array",\n'                
                        '}'
                    }
                ],
                max_tokens=4096, # Limits the maximum number of tokens in the generated response. The total number of tokens (incoming messages + generated tokens) must not exceed the limit for the selected model.
                temperature=1.0, # Controls the degree of "creativity" of the answer. Range of values: from 0 to 2.
                top_p=1.0, # Alternative to temperature. This parameter limits the selection of tokens to a certain probability percentile (also called "nucleus sampling"). Range: 0 to 1.
                model="gpt-4o"
            )
        result = json.loads(response.choices[0].message.content)
        return result
    except Exception as e:
        print(f"Error during summarization and topics retrieving: {e}")
        return None
    
# Function for demonstration of CHUNKS implementation
async def get_result_for_long_content_aticle():
    test_article = {
        "id" : 0,   
        "headline": "!!! DEMONSTRATION ARTICLE WITH LONG CONTENT. !!!",
        "content": "Artificial intelligence (AI) refers to the capability of computational systems to perform tasks typically associated with human intelligence, such as learning, reasoning, problem-solving, perception, and decision-making. It is a field of research in computer science that develops and studies methods and software that enable machines to perceive their environment and use learning and intelligence to take actions that maximize their chances of achieving defined goals. Such machines may be called AIs.\n"
                   "High-profile applications of AI include advanced web search engines (e.g., Google Search); recommendation systems (used by YouTube, Amazon, and Netflix); virtual assistants (e.g., Google Assistant, Siri, and Alexa); autonomous vehicles (e.g., Waymo); generative and creative tools (e.g., ChatGPT and AI art); and superhuman play and analysis in strategy games (e.g., chess and Go). However, many AI applications are not perceived as AI: A lot of cutting edge AI has filtered into general applications, often without being called AI because once something becomes useful enough and common enough it's not labeled AI anymore.\n"
                   "Various subfields of AI research are centered around particular goals and the use of particular tools. The traditional goals of AI research include learning, reasoning, knowledge representation, planning, natural language processing, perception, and support for robotics. General intelligence—the ability to complete any task performed by a human on an at least equal level—is among the field's long-term goals. To reach these goals, AI researchers have adapted and integrated a wide range of techniques, including search and mathematical optimization, formal logic, artificial neural networks, and methods based on statistics, operations research, and economics. AI also draws upon psychology, linguistics, philosophy, neuroscience, and other fields.\n"
                   "Artificial intelligence was founded as an academic discipline in 1956, and the field went through multiple cycles of optimism throughout its history, followed by periods of disappointment and loss of funding, known as AI winters. Funding and interest vastly increased after 2012 when deep learning outperformed previous AI techniques. This growth accelerated further after 2017 with the transformer architecture, and by the early 2020s many billions of dollars were being invested in AI and the field experienced rapid ongoing progress in what has become known as the AI boom. The emergence of advanced generative AI in the midst of the AI boom and its ability to create and modify content exposed several unintended consequences and harms in the present and raised concerns about the risks of AI and its long-term effects in the future, prompting discussions about regulatory policies to ensure the safety and benefits of the technology.",
        "summary": "",
        "topics": []
    }

    # Split content to chunks
    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(model_name="gpt-4o", chunk_size=500, chunk_overlap=10)
    chunks = text_splitter.split_text(test_article['content'])

    client = create_openip_client.create_openip_client() 

    # Generating tasks in a loop
    tasks = [sent_request_to_ai(client, chunk) for chunk in chunks]

    # Run tasks in parallel
    summarys_topics = await asyncio.gather(*tasks)

    summarys_topics_len = len(summarys_topics)
    for item in summarys_topics:  
        if item: 
            # Merge summarys string                    
            if 1 < summarys_topics_len-1:
                test_article["summary"] += item["summary"] + ' '
            else:
                test_article["summary"] += item["summary"]
            # Merge topic lists
            test_article["topics"] += item["topics"]

    return [test_article]

