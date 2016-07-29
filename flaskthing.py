import os 
# ^^ dis is how you access environment vars in Python: os.environ 

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Zane and Dad are burning the house down"

if __name__ == "__main__":
    #app.run()
    #app.run(host='0.0.0.0')
    #Be careful: http://flask.pocoo.org/docs/0.10/quickstart/ 
    
    #JK, trying this from http://stackoverflow.com/questions/17260338/deploying-flask-with-heroku: 
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
