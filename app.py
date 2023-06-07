from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/about")
def about():
    return "This is an about page"


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        print(f"Name: {name}\nEmail: {email}\nMessage: {message}")
    return render_template("contact.html")


app.run(port=8080)
