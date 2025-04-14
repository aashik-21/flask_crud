from flask import Flask, render_template,request,redirect
from  models import db, StudentModel
from flask import request
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app) 

# @app.before_first_request
def create_table():
    db.create_all()
with app.app_context():
    create_table()


@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "GET":
        return render_template("create.html")


    if request.method == "POST":
        hobby = request.form.getlist("hobbies")
        hobbies = ",".join(map(str, hobby))
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        password = request.form["password"]
        gender = request.form["gender"]
        hobbies = hobbies
        country = request.form["country"]

        student = StudentModel(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            gender=gender,
            hobbies=hobbies,
            country=country
        )
        db.session.add(student)
        db.session.commit()
        return redirect("/")

@app.route('/', methods =['GET','POST'])
def RetrieveList():
    students = StudentModel.query.all()
    print(students)
    return render_template("index.html",students=students)
    
app.run(host='localhost', port=5000 )