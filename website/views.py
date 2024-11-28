from flask import Blueprint, Flask, render_template, request, redirect, url_for
from .models import Todo
from . import db

my_view = Blueprint("my_view", __name__)

@my_view.route("/")
def home():
    todoList = Todo.query.all()
    errMessage = request.args.get("err", None)
    message = request.args.get("message", None)
    return render_template("index.html", todoList=todoList, err=errMessage, message=message)

@my_view.route("/add", methods=["POST"])
def add():
    try:
        task = request.form.get("task")
        newTodo = Todo(task=task)

        db.session.add(newTodo)
        db.session.commit()

        message = "Task added successfully"
        return redirect(url_for("my_view.home", message=message))

    except:
        message = "There are an error adding your task. Please try again"
        return redirect(url_for("my_view.home", err=message))

@my_view.route("/update/<todoId>")
def update(todoId):
    try:
        todo = Todo.query.filter_by(id=todoId).first()
        todo.complete = not todo.complete

        db.session.commit()
        message = "Task updated successfully"
        return redirect(url_for("my_view.home", message=message))
    except:
        message = "Something went wrong"
        return redirect(url_for("my_view.home", err=message))


@my_view.route("/delete/<todoId>")
def delete(todoId):
    try:
        todo = Todo.query.filter_by(id=todoId).first()
        
        db.session.delete(todo)
        db.session.commit()

        message = "Task updated successfully"
        return redirect(url_for("my_view.home", message=message))
    except:
        message = "Task wasn't deleted. Please try again"
        return redirect(url_for("my_view.home", err=message))

@my_view.route("/updateTask/<todoId>", methods=["POST"])
def updateTask(todoId):
    try:
        newTask = request.form.get("updatedTask")
        todo = Todo.query.filter_by(id=todoId).first()
        
        todo.task = newTask

        db.session.commit()
        message = "Task updated successfully"
        return redirect(url_for("my_view.home", message=message))
    except:
        message = "There was an error updating this task. Please try again"
        return redirect(url_for("my_view.home", err=message))