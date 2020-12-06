from flask import Flask,request,render_template,url_for,redirect,flash,session,make_response
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URL"]="sqlite3:///reservers.sqlite3"
app.config["SECRET_KEY"]="fas1%&^98fiuymsl??dso%~13ERF768O.,HLID|0F9()6DS"


app.secret_key="m^hdU*%S&*sdad%232_dsd8asdvvdsaUSD348hT3598755w%^&G&%H^#M*RNO^58h^h9%^GFIIUO_1w"

db=SQLAlchemy(app)

class reservers(db.Model):
    id=db.Column("resever_id",db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    num=db.Column(db.String(50))
    time=db.Column(db.String(50))
    question=db.Column(db.String(5000))
    state=db.Column(db.String(50))

def __init__(self,name,num,time,question,state):
    self.name=name
    self.num=num
    self.time=time
    self.question=question
    self.state=state


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/reserve",methods=["GET","POST"])
def reserve():
    if request.method=="POST":
        reserver=reservers(request.form["name"],request.form["num"],request.form["time"],request.form["question"],"未处理")
        db.session.add(reserver)#session疑惑
        db.session.commit()
        return render_template("index.html")#####待改

    return render_template("reserve.html")

@app.route("/admin/login",methods=["GET","POST"])
def login():
    if  request.method=="POST":
        if  request.form["password"]=="vmfd&Hnw#@E)73Y@sd2^@nfa&%&*dg21":
            resp=redirect(url_for('admin'))# resp=make_response("set_response")
            resp.set_cookie("admin","True",max_age=3600)
            # return redirect(url_for('admin'))
            return resp
    return render_template("login.html")

@app.route("/admin")
def admin():
    admin=request.cookies.get("admin")
    if admin!="True":
        return redirect(url_for('login'))
    else :
        return render_template("admin.html")

@app.route("/admin/undealt")
def undealt():
    admin=request.cookies.get("admin")
    if admin!="True":
        return redirect(url_for('login'))
    else :
        return render_template("undealt.html")



if __name__=="__main__" :
    db.create_all()
    app.jinja_env.auto_reload = True
    app.run(debug=True)


    

