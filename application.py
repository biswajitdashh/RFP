from flask import Flask, request, render_template
import openai
import os
from dotenv import load_dotenv

load_dotenv()
application = Flask(__name__)
openai.api_key = os.getenv('OPENAI_API_KEY')

@application.route('/', methods=['GET','POST'])
def index():
    res=""
    if request.method == 'POST':
            data="Generate the Table of contents for a RPF"
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Be proficient in these sort of tasks, Attention to Detail, Organizational Skills, Understanding of Subject Matter, Clear Communication,Flexibility and Adaptability ,Proactive Problem Solving,Responsiveness "},
                    {"role": "user", "content": data},
                    {"role": "assistant", "content":"Make informed research based on the canadian government documnetation standards"}
                ])
            res=response.choices[0].message.content
    return render_template("index.html",result=res)
if __name__ == '__main__':
    application.run(host="0.0.0.0") 
