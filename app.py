from flask import Flask,render_template,request,redirect,url_for    
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'

db=SQLAlchemy(app)

migrate=Migrate(app,db)

class Todo(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100),nullable=False)
    complete = db.Column(db.Boolean,default=False)

@app.route('/')
def home():
    #obj=Todo(title="Project1",complete=False)
    #db.session.add(obj)
    #db.session.commit()

    output=Todo.query.all() 
    return render_template("base.html",output=output)

@app.route('/add',methods=['POST'])
def add():
    title=request.form.get("Title")
    obj=Todo(title=title,complete=False)
    db.session.add(obj)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/update/<int:todo_id>")
def update(todo_id):
    obj=Todo.query.filter_by(id=todo_id).first()
    obj.complete=not obj.complete
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    obj=Todo.query.filter_by(id=todo_id).first()
    db.session.delete(obj)
    db.session.commit()
    return redirect(url_for("home"))

if __name__ == '__main__':
    app.run(debug=True)