from random import random
from flask import Flask, render_template, jsonify, request
from urllib import response
from chatbot.chat import get_response



app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chatbot', methods=["GET", "POST"])
def get_bot_response():
    if request.method == "POST":

            message = request.args.get('msg')
            response = ""
            if message:
                response = get_response(message)
                return str(response)
        


            else:
                return "I do not understand. Please try again."


if __name__=="__main__":
    app.run(debug=True)
