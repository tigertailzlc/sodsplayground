from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Zane and Dad are burning the house down"

if __name__ == "__main__":
    app.run()
