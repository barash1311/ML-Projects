from flask import Flask

# initialize the falask
#instance of the falsk app
 #it create an instacne of the falsk classs
#which will be your wsgi application
app=Flask(__name__)

#routes
@app.route("/")
def welcome():
    return "welcome to this flask course"

@app.route("/index")
def hello():
    return "hello index"
@app.route("/projects")
def projects():
    return "welcome to the project page"


#entry point
if __name__=="__main__":
    app.run(debug=True)