import requests
from send_email import send_email
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os

load_dotenv()

NEWS_API_KEY=os.getenv('NEWS_API_KEY')
GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')

url = 'https://newsapi.org/v2/top-headlines?'\
      'sources=techcrunch&'\
      f'apiKey={NEWS_API_KEY}&'\
      'language=en'

request = requests.get(url)
content=request.json()
article=content['articles']

model=init_chat_model(
    model='gemini-2.5-flash',
    model_provider='google_genai',
    api_key=GOOGLE_API_KEY
)

prompt=f'''
You are a news summarizer.
Give me 1st paragraph containing summary.
Give me 2nd paragraph describing how this tech is helping mankind.
Here are the articles {article}
'''

response=model.invoke(prompt)
response_str=response.content

msg=f'Subject: News Summarizer \n\n {response_str}'

msg = msg.encode('utf-8')
send_email(msg)