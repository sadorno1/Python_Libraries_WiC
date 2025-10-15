from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/hello", methods=["POST"])
def say_hello():
    name = request.form.get("username", "Stranger")
    return render_template("hello.html", name=name)

@app.route("/hello/<name>")
def hello_dynamic(name):
    return render_template("hello.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)
