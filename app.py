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

@app.route('/sketch')
def sketch():
    return render_template("sketch.html")

@app.route('/ipa')
def ipa():

    return render_template("ipa.html")

@app.route('/sokka')
def sokka():
    return render_template("sokka.html")

@app.route('/catchat')
def catchat():

    return render_template("catchat.html")

@app.route('/thanos_bot')
def thanos_bot():

    return render_template("thanos_bot.html")




@app.route('/tutor_bot')
def tutor_bot():
    return render_template("tutor_bot.html")

@app.route('/progress-chat')
def index():
    return render_template('progress-chat.html', image_path=IMAGE_PATH)


@app.route("/LebronChat")
def LebronChat():
    return render_template("LebronChat.html")

@app.route("/senator")
def senator():
    return render_template("senator.html")

@app.route("/fish")
def fish():
    return render_template("fish.html")

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