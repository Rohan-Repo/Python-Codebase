from flask import Flask, request, render_template, redirect

app = Flask(__name__)

registeredStudents = {}
# If we allow FE to give the values some hacker can change the values and wrong values could go into the DB
# To avoid this we can set the Sports here in BE and then just send that to FE
# We can add or Delete Sports in the future so this would definitely come in handy NO hard-coding
allowedSports = ["Badminton", "Basketball", "Football", "Baseball"]


@app.route("/")
def index():
    return render_template("index.html", plcSports=allowedSports)


@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    sport = request.form.get("sport")
    # If Name not provided or Sport not provided render the error page
    if not name:
        return render_template("incorrectSportError.html")
    elif sport not in allowedSports:
        return render_template("incorrectSportError.html")

    registeredStudents[name] = sport
    print(name, '-', sport)

    return render_template("success.html", plcName=name, plcSport=sport)


@app.route("/registrants")
def getAllRegistrants():
    return render_template("registeredStudents.html", registrants=registeredStudents)


# Create Admin Login and based on the Authentication we write below logic
@app.route("/adminPanel")
def adminPage():
    return render_template("adminPanel.html")


@app.route("/adminLogin", methods=["POST"])
def adminLoginPage():
    userName = request.form.get("userName")
    password = request.form.get("password")

    print(userName, ' - ', password)

    # For correct credentials, display all the registered students otherwise show Error Page
    if userName == "admin" and password == "admin":
        return redirect("/registrants")
    else:
        return render_template("incorrectAdminUser.html")
