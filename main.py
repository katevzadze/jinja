from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return ("Hello!")


@app.route("/logo/<name>/<surname>/<age>")
def logo(name, surname, age):
    return render_template("logo.html", name=name, surname=surname, age=age, title="приветствие")


if __name__ == '__main__':
    app.run()
