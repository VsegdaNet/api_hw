from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/clothing/")
def get_clothing():
    return render_template('clothing.html')


@app.route("/footwear/")
def get_footwear():
    return render_template('footwear.html')


@app.route("/jacket/")
def get_jacket():
    return render_template('jacket.html')


if __name__ == '__main__':
    app.run()