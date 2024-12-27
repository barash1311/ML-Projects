from flask import Flask,render_template,request
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>welcome to flask course</h1></html>"

@app.route("/index",methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/form",methods=["GET","POST"])
def form():
    if request.method=="POST":
        name=request.form['name']
        return f"hello {name}"
    return render_template("form.html")

@app.route("/name",methods=["GET","POST"])
def name():
    if request.method=="POST":
        name=request.form["name"]
        return f"hello {name}"
    return render_template("name.html")

    


if __name__=="__main__":
    app.run(debug=True)