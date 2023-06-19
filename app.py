from flask import Flask,render_template, redirect, request

app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def index():
    return render_template("index.html")

@app.route('/login',methods=["GET","POST"])
def login():
    return render_template("signin.html")

@app.route('/register',methods=["GET","POST"])
def register():
    return render_template("signup.html")

@app.route('/aboutus',methods=["GET","POST"])
def aboutus():
    return render_template("aboutus.html")

@app.route('/contactus',methods=["GET","POST"])
def contactus():
    return render_template("contactus.html")


if __name__ == "__main__":
    app.run()