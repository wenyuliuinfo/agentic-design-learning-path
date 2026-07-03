# Import libraries
import os
import json

from dotenv import load_dotenv
from openai import OpenAI
from serpapi import GoogleSearch

# Load env variable for API Key
load_dotenv()
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL")
SERP_API_KEY = os.getenv("SERP_API_KEY")

client = OpenAI(
    api_key=DEEPSEEK_API_KEY,
    base_url=DEEPSEEK_BASE_URL
)

# --- Step 1: Classify the Prompt ---
def classify_prompt(prompt: str) -> dict:
    """
    Classify the user prompt.
    """
    system_message = {
        "role": "system",
        "content": (
            "You are a classifier that analyzes user prompts and returns one of three categories ONLY:\n"
            " - simple\n"
            " - reasoning\n"
            " - internet_search\n"
            "Rules:\n"
            " - Use 'simple' for direct factual questions that need no reasoning or current events.\n"
            " - Use 'reasoning' for logic, math, physics, or multi-step inference questions.\n"
            " - Use 'internet_search' if the prompt refers to current events, recent data, or things not in your training data.\n\n"
            "Respond ONLY with JSON like:\n"
            '{"classification": "simple"}'
        ),
    }
    user_message = {"role": "user", "content": prompt}
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[system_message, user_message],
        temperature=1,
    )

    reply = response.choices[0].message.content
    return json.loads(reply)

# --- Step 2: Serp API Google Search ---
def google_search(query: str, num_results=1) -> list:
    """
    Function to define Google Search.
    """
    params = {
        "q": query,
        "location": "China",
        "hl": "en",
        "gl": "cn",
        "api_key": SERP_API_KEY
    }
    try:
        # Create the search object and execute it
        search = GoogleSearch(params)
        results = search.get_dict()
        if "organic_results" in results:
            return [
                {
                    "title": result.get('title'),
                    "link": result.get('link'),
                    "snippet": result.get('snippet'),
                }
                for result in results["organic_results"]
            ]
        else:
            return []
    except Exception as e:
        return {"error": str(e)}

# --- Step 3: Generate Response ---
def generate_response(prompt: str, classification: str, search_results=None) -> str:
    """
    Generate response based on user query classification.
    """
    if classification == "simple":
        model = "deepseek-v4-flash"
        full_prompt = prompt
        extra_body = {
            "thinking": {"type": "disabled"}
        }
    elif classification == "reasoning":
        model = "deepseek-v4-flash"
        full_prompt = prompt
        extra_body={
            "thinking": {"type": "enabled"}  
        }
    elif classification == "internet_search":
        model = "deepseek-v4-pro"
        # Convert search result dict to a readable string
        if search_results:
            search_context = "\n".join(
                [
                    f"Title: {item.get('title')}\nSnippet: {item.get('snippet')}\nLink: {item.get('link')}"
                    for item in search_results
                ]
            )
        else:
            search_context = "No search results found."
        extra_body={
            "thinking": {"type": "enabled"}  
        }
        full_prompt = f"""
            Use the following web results to answer the user query:
            {search_context}
            Query: {prompt}
        """
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": full_prompt}],
        temperature=1,
        extra_body=extra_body
    )
    return response.choices[0].message.content, model

# --- Step 4: Combined Router ---
def handle_prompt(prompt: str) -> dict:
    classification_result = classify_prompt(prompt)
    classification = classification_result["classification"]
    
    search_results = None
    if classification == "internet_search":
        search_results = google_search(prompt)
    
    answer, model = generate_response(prompt, classification, search_results)
    return {"classification": classification, "response": answer, "model": model}

test_prompt_1 = "What is the capital of Australia?"
test_prompt_2 = "Explain the impact of quantum computing on cryptography."
test_prompt_3 = "When does the Australian Open 2026 start, give me the full date?"

result = handle_prompt(test_prompt_2)
print("Classification:", result["classification"])
print("Model Used:", result["model"])
print("Response:", result["response"])