from flask import Flask, render_template, request
from numpy import require

#  RUN AS - python -m flask run
# __name__ indicates this file
app = Flask(__name__)

# @app.route("/")
# def homePage():
    # return "Hello World : Doesn't print out our HTML Page
    # return render_template("index.html")
    # This renders the webpage
    # If we pass the name through URL we get that using the request object
    # request.args has all the key-value pairs we sent via URL
    # if "name" in request.args:
    #     name = request.args["name"]
    # # Prints Hello Carter for I/P: http://127.0.0.1:5000/?name=Carter : <h2> Hello Carter </h2>
    # else:
    #     name = "World"
    # # Prints Hello World for no I/P given : <h2> Hello World </h2>
    # This one line gets the parameter name otherwise sets it to none
    # name = request.args.get("name");
    # But since we want it to have a default value of World we set it like below
    # name = request.args.get( "name", "World" );
    # This sets the parameter automatically otherwise gives it the value of World
    # return render_template("index.html", placeHolder1=name)
#     return render_template("greet.html")
#
# @app.route("/greet")
# def greetPage():
#     name = request.args.get("name", "World");
#     return render_template("index.html", placeHolder1=name)

# @app.route("/")
# def homePage():
#     return render_template("greetWithLayout.html")
#
# # Just Changing to POST Gives an error - 405 (METHOD NOT ALLOWED)
# #     For GET requests - request.args and For POST Requests - request.form
# @app.route("/greet", methods=["POST"])
# def greetPage():
#     # Instead of getting the values we need to grab the Form Request element
#     # name = request.args.get("name", "World");
#     name = request.form["name"];
#     # IF we don't give any input we want to set to a default value, this is how we do it
#     if len(name) == 0:
#         name = 'World'
#     return render_template("indexWithLayout.html", placeHolder1=name)

# If we want to Hide all URLS we can use GET and POST Together
# By default Redirected to / using the GET method
@app.route( "/", methods=["GET", "POST"] )
def homePage():
    if request.method == "GET":
        return render_template("greetWithLayout.html")
    elif request.method == "POST":
        name = request.form["name"];
        # IF we don't give any input we want to set to a default value, this is how we do it
        if len(name) == 0:
            name = 'World'

        return render_template("indexWithLayout.html", placeHolder1=name)