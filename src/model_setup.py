from langchain.chat_models import ChatOpenAI  

def get_custom_llm(openai_api_key, model_name):
    return ChatOpenAI(
        model_name=model_name,
        openai_api_key=openai_api_key  
    )
