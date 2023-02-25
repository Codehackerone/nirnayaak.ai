import os
import openai
import json
from dotenv import load_dotenv


def configure():
    load_dotenv("venv/.env")


openai.api_key = f"{os.getenv(OPENAI_APIKEY)}"


def get_judement(search_text):
    try:
        prompt = f"Give a judgment on the basis of Indian Constitution. Add sections in response. Do not reply something controversial. {search_text}"

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return response["choices"][0]["text"].strip()
    except:
        return "cannot reply"


def get_title_date_parties(doc_text) :
    try :
        doc_text = doc_text.split()
        prompt = f"Give a title, parties involved, court name, and date from the below text in json format only.{doc_text}"
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        string_json = response["choices"][0]["text"].strip()
        return_json = json.loads(string_json)
        return return_json
    except :
        return "cannot reply"