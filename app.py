from flask import Flask, redirect, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskTodoList.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String , nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/', methods=[ 'GET', 'POST'])

def index():
    if request.method == 'POST':
        task_content = request.form['content']
        newTask = Todo(content=task_content)

        try:
            db.session.add(newTask)
            db.session.commit()
            return redirect('/')
        except:
            return "There was an issue adding your Todo."
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:id>')

def deleteTask(id):
    taskDelete = Todo.query.get_or_404(id)

    try:
        db.session.delete(taskDelete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was an error deleting the Task'
@app.route('/update/<int:id>', methods=['GET', 'POST'])

def updateTask(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an error updating your task'
        
    else:
        return render_template('update.html', task=task)



if __name__ == "__main__":
    app.run(debug=True)