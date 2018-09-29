from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.categories.models import Category
from application.auth.models import User
from application.categories.forms import CategoryForm, EditForm

@app.route("/categories", methods=["GET"])
@login_required
def categories_index():
    return render_template("categories/list.html", categories = Category.query.all(), id = current_user.id)

@app.route("/categories/new/")
@login_required
def categories_form():
    return render_template("categories/new.html", form = CategoryForm())

@app.route("/categories/", methods=["POST"])
@login_required
def categories_create():
    form = CategoryForm(request.form)
 
    if not form.validate():
        return render_template("categories/new.html", form = form)

    c = Category(form.name.data)
    c.account_id = current_user.id
  
    db.session().add(c)
    db.session().commit()

    return redirect(url_for("categories_index"))

@app.route("/categories/edit/<category_id>/", methods=["POST"])
@login_required
def categories_edit(category_id):
    form = EditForm(request.form)

    c = Category.query.get(category_id)

    if not form.validate():
        return render_template("categories/edit.html", category = c, form = form)

    c.name = form.name.data
    c.account_id = current_user.id

    db.session().commit()

    return redirect(url_for("categories_index"))

@app.route("/categories/remove/<category_id>/", methods=["POST"])
@login_required
def categories_remove(category_id):

    c = Category.query.get(category_id)
    db.session().delete(c)
    db.session().commit()
  
    return redirect(url_for("categories_index"))
