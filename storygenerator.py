from langchain import PromptTemplate, LLMChain
from langchain_community.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()

def generate_story(scenario):
    template = '''
    You are a story teller;
    You can generate a short story based on a simple narrative. 
    The story should be no more than 20 words.

    CONTEXT: {scenario}
    STORY:
    '''
    prompt = PromptTemplate(template=template, input_variables=["scenario"])

    # Use LLM to generate a story based on the given scenario
    story_llm = LLMChain(
        llm=ChatOpenAI(
            openai_api_key=os.getenv("OPENAI_API_KEY"), 
            model_name="gpt-3.5-turbo", 
            temperature=1
        ), 
        prompt=prompt, 
        verbose=True
    )
    story = story_llm.predict(scenario=scenario)
    print(story)
    return story
