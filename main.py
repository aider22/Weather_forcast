from flask import Flask, render_template, request, url_for, redirect


app = Flask(__name__)

dict = {}


@app.route('/')
def main():
    return render_template('index.html')


@app.get("/creation")
def creation_to():
    return redirect(url_for("main"))


@app.get("/authorization")
def authorization_to():
    return redirect(url_for("main"))


@app.get("/creation")
def creation():
    nickname = request.form.get("nickname")
    email = request.form.get("email")
    password = request.form.get("password")

    if nickname or email in dict:
        print("Ви вже зареєстровані, виконайте вхід.")
    else:
        dict.add(creation())
        print("Nickname ->", nickname,
            "Email ->", email,
            "Password ->", password)
        return render_template('creation.html')


@app.get("/authorization")
def authorization():
    nickname = input("Nickname: ")
    password = input("Password: ")
    if nickname and password in dict:
        print("Вхід виконано")
    else: 
        print("Не вірна інформація, спробуйте ще раз.")
    return render_template('creation.html')


if __name__ == "__main__":
    app.run(
        host='127.0.0.3',
        port="3030",
        debug=True
    )