from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.tasks.models import Task
from application.auth.models import User
from application.categories.models import Category
from application.tasks.forms import TaskForm, EditForm
from application.categories.forms import CategoryForm


@app.route("/tasks", methods=["GET"])
@login_required
def tasks_index():
    return render_template("tasks/list.html", tasks = Task.query.all(), id = current_user.id)

@app.route("/tasks/new/")
@login_required
def tasks_form():
    categories = [(category.id, category.name) for category in Category.query.all()]
    form = TaskForm()
    form.tasks_and_categories.choices = categories
    return render_template("tasks/new.html", form = form)
  
@app.route("/tasks/<task_id>/", methods=["POST"])
@login_required
def tasks_set_done(task_id):

    t = Task.query.get(task_id)
    t.done = True
    db.session().commit()
  
    return redirect(url_for("tasks_index"))

@app.route("/tasks/", methods=["POST"])
@login_required
def tasks_create():
    form = TaskForm(request.form)
    form.tasks_and_categories.choices = [(category.id, category.name) for category in Category.query.all()]
 
    if not form.validate():
        return render_template("tasks/new.html", form = form)

    t = Task(form.name.data, form.priority.data, Category.all_by_id(form.tasks_and_categories.data))
    t.done = form.done.data
    t.account_id = current_user.id
  
    db.session().add(t)
    db.session().commit()

    return redirect(url_for("tasks_index"))

@app.route("/tasks/edit/<task_id>/", methods=["POST"])
@login_required
def tasks_edit(task_id):
    form = EditForm(request.form)

    t = Task.query.get(task_id)

    if not form.validate():
        return render_template("tasks/edit.html", task = t, form = form)

    t.name = form.name.data
    t.priority = form.priority.data
    t.done = form.done.data
    t.account_id = current_user.id

    db.session().commit()

    return redirect(url_for("tasks_index"))

@app.route("/tasks/remove/<task_id>/", methods=["POST"])
@login_required
def tasks_remove(task_id):

    t = Task.query.get(task_id)
    db.session().delete(t)
    db.session().commit()
  
    return redirect(url_for("tasks_index"))
