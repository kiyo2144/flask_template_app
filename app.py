from flask import Flask, request

app = Flask(__name__)

# ルートデコレーションが無いため、ルートは表示されない


# [URL]/loginページを表示すると"login page"が表示される
@app.route("/login", methods=["GET", "POST"])
def login():
    # [URL]/loginページを表示するとPythonターミナルに"-----[GET or POST]-----"が表示される

    # print(f"-----{request.method}-----")
    if request.method == "GET":
        # return "login page"
        return """
        <form action="/login" method="post">
            Password:<input type="password" name="password"><br>
            <input type="submit">
        </form>
        """

    return "Logged in"


if __name__ == "__main__":
    app.run(port=8000)
