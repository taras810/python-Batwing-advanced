from app import app
from helpers.file import get_users, write_users
from flask import render_template, request, redirect


@app.route("/")
def main():
    users = get_users()
    return render_template("index.html", users=users)


@app.route("/user-add")
def user_add():
    return render_template("user-add.html")


@app.route("/users", methods=["POST"])
def save_user():
    users = get_users()
    id = 1
    if len(users) > 0:
        id = len(users) + 1
    user = {
        "id": id,
        "email": request.form.get("email"),
        "first_name": request.form.get("first_name"),
        "last_name": request.form.get("last_name"),
        "work_area": request.form.get("working_area")
    }
    users.append(user)
    write_users(users)
    return redirect("/")


@app.route("/user-edit/<int:id>")
def edit(id):
    users = get_users()
    for user in users:
        if user["id"] == id:
            return render_template("user-add.html", user=user)
    return redirect("/")


@app.route("/users/<int:id>", methods=["POST"])
def update(id):
    users = get_users()
    for user in users:
        if user["id"] == id:
            user["email"] = request.form.get("email")
            user["first_name"] = request.form.get("first_name")
            user["last_name"] = request.form.get("last_name")
            user["work_area"] = request.form.get("working_area")
    write_users(users)
    return redirect("/")


@app.route("/users/delete/<int:id>")
def delete(id):
    users = get_users()
    for user in range(len(users)):
        if users[user]['id'] == id:
            del users[user]
            break
    write_users(users)
    return redirect("/")


@app.route("/search", methods=["GET"])
def search():
    search_param = list(request.args.get("search").split(" "))
    users = get_users()
    results = []
    unique_result = []

    if search_param:
        for user in users:
            for value in user.values():
                for param in search_param:
                    if param.lower() in str(value).lower():
                        results.append(user)

    for x in results:
        if x not in unique_result:
            unique_result.append(x)

    if len(results) > 0:
        return render_template("search_result.html", users=unique_result)
    else:
        return render_template("search_result.html", no_res="No Results Found")
