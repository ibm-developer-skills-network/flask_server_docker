from flask import Flask
from os import environ 

username = environ.get('username',"the Learner")

app = Flask("My Flask Application")

@app.route("/")
def hello():
    return "<h1>This is the {}'s first cloud application</h1>".format(username)
    
if __name__=="__main__":
    app.run(debug=True) 
    # When no port is specified, starts at default port 5000
