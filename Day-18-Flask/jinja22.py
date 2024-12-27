#building url dynamically
#variable rule
#jinja2 template engine


'''there are multiple ways to read the data from the backed
1.{{ input}}
2.{%...%} conditions,loops
{#  ##} single line comments

'''
from flask import Flask,render_template,request,redirect,url_for
app=Flask(__name__)
@app.route("/")
def welcome():
    return "<html><h1> welcome to the flask page</h1></html>"

@app.route("/about")
def about():
    return render_template("about.html")
# @app.route("/submit",methods=["GET","POST"])
# def submit():
#     if request.method=="POST":
#         name=request.form["name"]
#         return f"hello {name}"
#     return render_template("form.html")

#variable rule
@app.route("/success/<int:score>")
def success(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"
    return render_template("result.html",results=res)

@app.route("/successresult/<int:score>")
def successess(score):
    res=""
    if score>=50:
        res="PASSED"
    else:
        res="FAILED"
    expressiion={"score":score,"res":res}
    return render_template("getresult.html",results=expressiion)

@app.route("/successif/<int:score>")
def if_success(score):
    return render_template("result1.html",results=score)

@app.route("/fail/<int:score>")
def fail(score):
    return render_template("result1.html",results=score)

@app.route("/submit",methods=["POST","GET"])
def submit():
    total_score=0
    if request.method=="POST":
        science=float(request.form["science"])
        maths=float(request.form["maths"])
        c=float(request.form["c"])
        data_science=float(request.form["datascience"])
        total_score=(science+maths+c+data_science)/4
    else:
        return render_template("getresult.html")
    return redirect(url_for("successess",score=total_score))
    


if __name__=="__main__":
    app.run(debug=True)