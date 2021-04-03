from flask import Flask
import random

ran_number = random.randint(0, 9)
# print(ran_number)

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Guess a number between 0 to 9: </h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

@app.route('/<int:num>')
def guess(num):
    if num < ran_number:
        return '<h1>Too low, Guess again</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'

    elif num > ran_number:
        return '<h1>Too High, Guess again</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'

    else:
        return '<h1>Wohhhlaa! You are correct</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=True)