from collections import namedtuple
from datetime import date
from time import time

from flask import Flask, request

"""
from time import time:
This syntax imports only the time function from the time module.
import time:
This syntax imports the entire time module.
"""

app = Flask(__name__)


@app.route("/")
def index():
    return {"Test": "This is an example",
            "Date": date.today(),
            "Timestamp": time()}


@app.route('/chat')
def chat():
    user_input: str = request.args.get('user_input')
    resource: Response = generate_response(user_input)
    json = {
        'input': user_input,
        'response': resource.response,
        'accuracy': resource.accuracy
    }
    return json


Response = namedtuple('Response', 'response, accuracy')


def generate_response(user_input: str) -> Response:
    lo_input: str = user_input.lower()
    if lo_input == 'hello':
        return Response('Hey there!', 100)
    elif lo_input == 'goodbye':
        return Response('Goodbye! Have a great day!', 100)
    else:
        return Response('I am sorry. I do not understand.', 0)


if __name__ == '__main__':
    app.run()
