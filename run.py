from flask import Flask,render_template,request,session,logging,url_for,redirect
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker

#from passlib.hash import sha256_crypto
engine=create_engine("mysql+pymysql://root:medtronic@localhost/flask_jinja")
#mysql+pymysql://username:password@localhost/db_name
db=scoped_session(sessionmaker(bind=engine))
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == "POST":
        name=request.form.get('name')
        username=request.form.get('username')
        password=request.form.get('password')
        confirm=request.form.get('confirm')

        if password==confirm:
            db.execute("insert into users(name,username,password) values(:name,:username,:password)",{"name":name,"username":username,"password":password})
            db.commit()
            return redirect(url_for('login'))
            
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)