from flask import Flask, render_template
app = Flask(__name__)
from flask import request
from datetime import datetime
from models import Question

questions = [
    Question("What is Python?", ["Snake", "Programming Language", "Car", "Food"], "Programming Language"),
    Question("2 + 2 = ?", ["3", "4", "5", "6"], "4"),
    Question("Which is a data structure?", ["Loop", "Queue", "Print", "Input"], "Queue"),
    Question("which of the following is not a programming language", ["Python", "Java", "HTML", "C++"], "HTML"),
    Question("which of these is an example of an output function in python?", ["input()", "print()", "len()", "type()"], "print()"),
    Question("which of these is an example of an output device?", ["Monitor", "Keyboard", "Mouse", "Scanner"], "Monitor"),
]
import random
random.shuffle(questions)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/test", methods=["GET", "POST"])
def test():
    username = request.args.get("username")
    
    if request.method == "POST":
        score = 0

        for i, question in enumerate(questions):
            answer = request.form.get(f"q{i}")
            if answer == question.answer:
                score += 1

        time_submitted = datetime.now().strftime("%H:%M")

        return render_template(
            "result.html",
             score=score,
             total=len(questions),
             time=time_submitted,
             username=request.form.get ("username")
        )
    return render_template("test.html", questions=questions, username=username)

if __name__ == "__main__":
    app.run(debug=True)