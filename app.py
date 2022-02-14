from flask import Flask, redirect, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

import os

username = os.environ['PGUSER']
password = os.environ['PGPASSWORD']

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://PGPASSWORD@PGUSER/flaskTodoList'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')
    
if __name__ == "__main__":
    app.run(debug=True)