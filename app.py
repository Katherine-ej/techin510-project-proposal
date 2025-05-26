from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/habit-tracker')
def habit_tracker():
    return render_template("habit_tracker.html")

@app.route('/tomato-clock')
def tomato_clock():
    return render_template("tomato_clock.html")

@app.route('/todo-list')
def todo_list():
    return render_template("todo_list.html")

if __name__ == "__main__":
    app.run(debug=True)
