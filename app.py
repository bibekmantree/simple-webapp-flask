import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "OMM NAMHA Haribolo!"

@app.route('/how are you')
def hello():
    return 'Hari Hari kara pari'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
