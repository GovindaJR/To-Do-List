from app import app, db
from flask import redirect, render_template, url_for, flash, request
from app.form import AddTask
from app.database import Task


# Main Page
@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home():
    form = AddTask()
    if request.method == "POST":
        task = form.add_task.data
        db.session.add(Task(task=task))
        db.session.commit()
        flash("Task Added!", "success")
        return redirect(url_for("home"))
    else:
        return render_template("index.html", form=form, Task=Task)


@app.route("/edit/<id>", methods=["GET", "POST"])
def edit(id):
    task = Task.query.get(id)
    if request.method == "POST":

        if "update" in request.form:
            updated_task = request.form["edit_field"]
            task.task = updated_task
            db.session.commit()
            flash("Updated Task!", "primary")
            return redirect(url_for("home"))

        elif "delete" in request.form:
            db.session.delete(task)
            db.session.commit()
            flash("Task Deleted!", "danger")
            return redirect(url_for("home"))
    else:
        return render_template("edit.html", task=task)






