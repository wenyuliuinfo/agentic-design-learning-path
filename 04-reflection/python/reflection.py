import os
import asyncio
from typing import Optional

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv

# --- Configuration ---
load_dotenv()
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL")


llm = ChatOpenAI(
    model="deepseek-v4-pro",  # Or "deepseek-v4-flash" for a faster option
    openai_api_key=DEEPSEEK_API_KEY,
    openai_api_base=DEEPSEEK_BASE_URL, 
    temperature=0.1
)

def run_reflection_loop():
    """
    Demonstrates a multi-step AI reflection loop to progressively improve a Python function.
    """
    
    # --- The Core Task ---
    task_prompt = """
    Your task is to create a Python function named 'calculate_factorial'.
    1. Accept a single integer 'n' as input.
    2. Calculate its factorial (n!).
    3. Include a clear docstring explaining what the function does.
    4. Handle edge cases: The factorial of 0 is 1.
    5. Handle invalid input: Raise a ValueError if the input is a negative number.
    """

    # --- The Reflection Loop ---
    max_iterations = 3
    current_code = ""
    message_history = [HumanMessage(content=task_prompt)]
    
    for i in range(max_iterations):
        print("\n" + "="*25 + f" REFLECTION LOOP: ITERATION {i+1} " + "="*25)

        # --- 1. Generate/Refine Stage ---
        if i == 0:
            print("\n>>> STAGE 1: GENERATING initial code...")
            response = llm.invoke(message_history)
            current_code = response.content
        else:
            print("\n>>> STAGE 1: REFINING code based on previous critique...")
            message_history.append(HumanMessage(content="Please refine the code using the critiques provides."))
            print(message_history)
            response = llm.invoke(message_history)
            current_code = response.content
        print("\n--- Generated Code ---\n" + current_code)
        message_history.append(response)

        # --- 2. Reflect Stage ---
        print("\n>>> STAGE 2: REFLECTING on the generated code...")
        reflector_prompt = [
            SystemMessage(content="""
                You are a senior software engineer and an expert in Python.
                Your role is to perform a meticulous code review. Critically evaluate
                the provided Python code based on the original task requirements.
                Look for bugs, style issues, missing edge cases, and areas for improvement.
                If the code is perfect and meets all requirements, respond with the single
                phrase 'CODE_IS_PERFECT'.
                Otherwise, provide a bulleted list of your critiques.
            """
            ),
            HumanMessage(content=f"Original Task:\n{task_prompt}\n\nCode to Review:\n{current_code}")
        ]
        critique_response = llm.invoke(reflector_prompt)
        critique = critique_response.content

        # --- 3. Stopping Condition ---
        if "CODE_IS_PERFECT" in critique:
            print("\n--- Critique ---\nNo further critiques found. The code is satisfactory.")
            break
        print("\n--- Critique ---\n" + critique)
        message_history.append(HumanMessage(content=f"Critique of the previous code: {critique}"))

    print("\n" + "="*30 + " FINAL RESULT " + "="*30)
    print(current_code)

if __name__ == "__main__":
    run_reflection_loop()