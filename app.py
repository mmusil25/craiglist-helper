from view import the_gui
from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello_world():
    the_gui()
    print('Exiting Program')
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
    app.run()