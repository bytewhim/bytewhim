from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

def authenticate_user(username, password):
    api_url = "http://localhost:8081/api/login"  
    data = {"username": username, "password": password}
    response = requests.post(api_url, json=data)
    return response.json()

def register_user(name, email, username, password):
    api_url = "http://localhost:8082/api/register"
    data = {"name": name, "email": email, "username": username, "password": password}
    response = requests.post(api_url, json=data)
    return response.json()

def add_review(bookname, author, review):
    api_url = "http://localhost:8084/api/reviews"
    data = {"book_title": bookname, "author": author, "review": review}
    response = requests.post(api_url, json=data)
    return response.json()

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        auth_result = authenticate_user(username, password)
        if auth_result.get("success"):
            return redirect(url_for("addreview"))
        else:
            error = auth_result.get("message")
    return render_template("login.html", error=error)

@app.route("/register", methods=["GET", "POST"])
def register():
    error = None
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        username = request.form["username"]
        password = request.form["password"]
        register_result = register_user(name, email, username, password)
        if register_result.get("success"):
            return redirect(url_for("login"))
        else:
            error = register_result.get("message")
    return render_template("register.html", error=error)

@app.route("/addreview", methods=["GET", "POST"])
def addreview():
    error = None
    if request.method == "POST":
        bookname = request.form["bookname"]
        author = request.form["author"]
        review = request.form["review"]
        review_result = add_review(bookname, author, review)
        if review_result.get("success"):
            return redirect(url_for("viewreview"))
        else:
            error = review_result.get("message")
    return render_template("addreview.html", error=error)

@app.route("/viewreview", methods=["GET"])
def viewreview():
    response = requests.get("http://localhost:8083/api/reviews")
    return  render_template("viewreview.html", json_response=response.json()) #response.json()

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
