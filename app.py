from flask import Flask, jsonify,request,jsonify,render_template,redirect
from flask_mysqldb import MySQL
from datetime import datetime
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token


app=Flask(__name__)

app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='medtronic'
app.config['MYSQL_DB']='flask_jinja'
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_CURSORCLASS']='DictCursor'
#app.config['MYSQL_PORT']='3306'
app.config['JWT_SECRET_KEY']='secret'


mysql=MySQL(app)
bcrypt=Bcrypt(app)
jwt=JWTManager(app)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register',methods=['GET','POST'])
def register():
    print("Hello")
    if request.method == "POST":
        
        name=request.form.get('name')
        username=request.form.get('username')
        password=request.form.get('password')
        confirm=request.form.get('confirm')
        print(name)

        if password==confirm:
            cur=mysql.connection.cursor()
            print(cur)
            #cur.execute("insert into users(name,username,password) values(:na)",{"name":name,"username":username,"password":password},(str(first),str(last),str(email),str(password),str(created)))
            query="insert into users(name,username,password) values('"+str(name)+"','"+str(username)+"','"+str(password)+"')"
            print(query)
            cur.execute(query)
            mysql.connection.commit()

            return render_template('login.html')
            
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)