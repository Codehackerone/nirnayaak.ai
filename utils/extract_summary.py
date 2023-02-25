import os
import cohere

COHERE_API_KEY = f"{os.getenv('cohere_api_key')}"
co_client = cohere.Client(COHERE_API_KEY)

def make_summary(text) :
    response = co_client.summarize(
        text=text,
        model='summarize-xlarge',
        length='medium',
        extractiveness='medium'
    )
    try :
        print(response.summary)
    except Exception as e :
        print(e)