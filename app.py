from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)

@app.route("/test")
def test():
    return render_template("test.html", questions=questions)

from models import Question
questions = [
    Question("What is Python?", "Programming Language"),
    Question("What is 2 + 2?", "4"),
    Question("Which is a data structure?", "Queue")
]