from flask import Flask
from flask import render_template
from flaskwebgui import FlaskUI # import FlaskUI

app = Flask(__name__)
ui = FlaskUI(app, width=500, height=500) # add app and parameters


@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/home", methods=['GET'])
def home():
    return render_template('some_page.html')


if __name__ == "__main__":
    # app.run() for debug
    ui.run()