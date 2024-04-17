from flask import Flask, render_template, request
from openai import OpenAI
import json

app = Flask(__name__)
client = OpenAI()


@app.route('/')
def index():
    # key = os.environ.get('OPENAI_API_KEY')
    # return key
    return render_template('index.html')

@app.route('/progress')
def progress():
    return render_template('progress-chat.html')

@app.route('/prof')
def prof():

    return render_template("prof.html")

@app.route('/prep')
def prep():

    return render_template("prep.html")

@app.route('/ipa')
def ipa():

    return render_template("ipa.html")

@app.route('/catchat')
def catchat():

    return render_template("catchat.html")

@app.route('/thanos_bot')
def thanos_bot():

    return render_template("thanos_bot.html")

@app.route("/chat")
def chat_completion():
    prompt = request.args.get('prompt')
    # parse data
    messages = json.loads(prompt)
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return str(completion.choices[0].message.content)


if __name__ == '__main__':
    app.run(debug=True)