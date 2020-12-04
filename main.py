from flask import Flask,request,render_template,url_for,redirect,flash
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URL"]="sqlite3:///reservers.sqlite3"
app.config["SECRET_KEY"]="fas1%&^98fiuymsl??dso%~13ERF768O.,HLID|0F9()6DS"

db=SQLAlchemy(app)

class reservers(db.Model):
    id=db.Column("resever_id",db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    num=db.Column(db.String(50))
    time=db.Column(db.String(50))
    question=db.Column(db.String(5000))

def __init__(self,name,num,time,question):
    self.name=name
    self.num=num
    self.time=time
    self.question=question


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/reserve",methods=["GET","POST"])
def reserve():
    if request.method=="POST":
        reserver=reservers(request.form["name"],request.form["num"],request.form["time"],request.form["question"])
        db.session.add(reserver)#session疑惑
        db.session.commit()
        return render_template("index.html")#####待改

    return render_template("reserve.html")


if __name__=="__main__" :
    db.create_all()
    app.run(debug=True)


    

