from flask import Flask, render_template, request, url_for, redirect
from user_functions import users

test = users()
app = Flask(__name__)




@app.route("/")
def home():
    return redirect(url_for("signup"))

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == "POST":
        user = request.form["Username"]
        password = request.form["Password"]
        email = request.form["Email"]

        firstname = request.form["Firstname"]
        lastname = request.form["Lastname"]
        currentcity = request.form["Currentcity"]
        currentcountry = request.form["Currentcountry"]

        if test.verifying_email_and_user_are_available( user, currentcity, currentcountry, email, firstname, lastname, password):
            
            return "thanks for registering"
        else:
            return "fields in use"
            

    
    else:
        return render_template("signup.html")




@app.route("/login",  methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        user = request.form["Username"]
        password = request.form["Password"]
        test.authincate_user(user, password)
        return "you have logged in"
    else:
         return render_template("login.html")


    

# @app.route("/after_login")
# def after_login(usr):
#     print(usr)
#     return f"hey {usr} thanks for registering !!"

    
 


if __name__ == "__main__":
    app.run(debug=True)

