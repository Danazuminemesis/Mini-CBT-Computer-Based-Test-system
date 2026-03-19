from flask import Flask, render_template
app = Flask(__name__)
from flask import request
from datetime import datetime

@app.route("/")
def home():
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)

@app.route("/test", methods=["GET", "POST"])
def test():
    if request.method == "POST":
        score = 0

        for i, question in enumerate(questions):
            answer = request.form.get(f"q{i}")
            if answer == question.answer:
                score += 1

        time_submitted = datetime.now().strftime("%H:%M")

        return render_template("result.html", score=score, total=len(questions), time=time_submitted)

    return render_template("test.html", questions=questions)

from models import Question
questions = [
    Question("What is Python?", "Programming Language"),
    Question("What is 2 + 2?", "4"),
    Question("Which is a data structure?", "Queue")
]