from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/user/<name>")
def hello(name):
    return render_template("hello.html", name=name)


@app.route("/members")
def members():
    # リストの作成
    members = ["Bob", "Tom", "Ken"]
    # 変数membersを渡してあげる
    return render_template("members.html", members=members)


if __name__ == "__main__":
    app.run(port=8000)

# Jinja2でhtmlに表示
