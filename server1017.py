from flask import Flask, render_template
import bitutil.stu

app = Flask(__name__)

@app.route("/hello/<irum>")
def helle(irum):
    #return render_template("hello.html",name=irum)
    return bitutil.stu.listStudent(irum)

@app.route("/insert",methods=["POST"])
def insert():
    name= request.form['name']
    kor = int(request.form['kor'])
    eng = int(request.form['eng'])
    math = int(request.form['math'])
    doc = {"name":name, "kor":kor,"eng":eng}

@app.route("/listStudent")
def listStudent():
    return bitutil.stu.listStudent()

@app.route("/")
def index():
    return "hello"

if __name__ == "__main__":
    app.run()