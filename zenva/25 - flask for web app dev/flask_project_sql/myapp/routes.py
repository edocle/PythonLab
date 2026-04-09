from flask import render_template, redirect, url_for, request
from myapp import app, db
from myapp.models import Task
from myapp.forms import Taskform

@app.route('/task', methods = ['GET', 'POST'])
def task():
    form = Taskform()
    if form.validate_on_submit():
        new_task = Task(
            title = form.title.data,
            description = form.description.data,
            is_complete = form.is_complete.data,
            priority = form.priority.data
        )
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('display_tasks'))
    return render_template('task.html', form=form)

@app.route('/task/list')
def display_tasks():
    tasks = Task.query.order_by(Task.priority.desc()).all()
    return render_template('task_list.html', tasks=tasks)

@app.route('/task/update_priority/<int:task_id>', methods = ["POST"])
def update_task_priority(task_id):
    task = Task.query.get_or_404(task_id)
    task.priority = int(request.form['priority'])
    db.session.commit()
    return redirect(url_for('display_tasks'))

@app.route('/task/update_status/<int:task_id>', methods = ["POST"])
def update_task_status(task_id):
    task = Task.query.get_or_404(task_id)
    task.is_complete = 'is_complete' in request.form
    db.session.commit()
    return redirect(url_for('display_tasks'))

@app.route('/task/delete/<int:task_id>', methods = ["POST"])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('display_tasks'))

@app.route('/helloworld')
def hello_world():
    return 'Hello, World!'

@app.route('/user/<username>')
def user(username):
    personal = f"<h1>Hello, {username}!</h1>"
    instruction = "<p>change the name in the <em> browser address bar </em> to see the effect.</p>"
    return personal + instruction

@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)

@app.route('/users')
def users():
    user_names = ['Alice', 'Bob', 'Charlie', 'David']
    return render_template('users.html', users=user_names)