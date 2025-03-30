# NewsParser

## Description  
This project provides a complete pipeline for extracting, summarizing, and semantically searching news articles using GenAI tools like OpenAI's GPT models. The focus is on integrating state-of-the-art AI tools to extract and process news articles from a predefined news site, generate summaries, identify topics, and provide powerful semantic search functionality.

---

## Features  
- **News Extraction**  
  - Scrapes news articles from a predefined news website.
  - Extracts both the headline and full text from the articles.

- **GenAI-Driven Summarization and Topic Identification**  
  - Summarizes the key points of news articles using GPT models or any other GenAI tools.
  - Identifies the main topics of each article.

- **Semantic Search with GenAI**  
  - Stores extracted news, generated summaries, and topics in a vector database.  
  - Provides a semantic search feature that interprets user queries and matches them with relevant articles.  
  - Understands nuances like context and semantic similarity (e.g., handling synonyms effectively).

---

## Requirements  
### Repository  
  Сlone the repository from [https://github.com/ANevelski/NewsParser.git](https://github.com/ANevelski/NewsParser.git).

### Environment Setup  
1. **Python Environment:**  
   Run the code in **VS Code**. Install the required libraries specified in `requirements.txt`:  
    ```bash
    beautifulsoup4 
    requests 
    openai 
    langchain-community 
    langchain-openai
    faiss-cpu
2. **Environment Variables File (.env):**
  Create a .env file in the root directory and specify the following keys:
    ```bash
    AZURE_OPENAPI_KEY={your Azure Resource Group API Key (Keys and Endpoint)}
    NEWS_SITE_URL={URL of the news website. Example: https://www.bbc.com/news} - A site should follows this structure for articles: Headlines in **<h2>** tags. Article text in **<p>** tags.
    USER_QUESTION_FOR_SEARCH={User query for semantic search, e.g., "Myanmar news"}

### Azure Models
Make sure the following models are enabled in Azure OpenAI services:
    ```bash
    gpt-4o
    text-embedding-3-large

### Vector Database
  The vector data for articles (summaries, topics) is stored in a local file named **"News_faiss_index"**. Ensure the application has sufficient permissions to create and write to this file.
  
### Application Entry Point
  The main script for the application is app.py.
