from flask import Flask


app = Flask(__name__)


@app.route("/") # главная страница сайта
def index():
    return "Hello, world!"

@app.route("/info")
def info():
    return "Меня создала компания GeekBrains!"

if __name__ == "__main__":
    app.run()