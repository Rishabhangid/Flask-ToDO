from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# initializing flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Defining the Todo model
class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

# defining routes
@app.route("/", methods=["GET","POST"])
def hello_world():
    if request.method == "POST":
      print(request.form['title'])
      print(request.form['descc'])
      task_add = request.form['title']
      desc_add = request.form['descc']
      # todo = Todo(title="First todo", desc="This is a page.")
      todo = Todo(title= task_add, desc= desc_add)
      db.session.add(todo)
      db.session.commit()

    allTodo = Todo.query.all()
    # allTodo = Todo.query.deleteAll()
    # print(allTodo)
    return render_template("index.html", alltodo = allTodo)



@app.route("/showproduct")
def products():
    allTodo = Todo.query.all()
    # Todo.query.delete()
    # db.session.commit()

    print(allTodo)
    return "Products"

@app.route("/delete/<int:sno>")
def delete_task(sno):
    # print(sno)
    toDelete = Todo.query.filter_by(sno = sno).first()
    db.session.delete(toDelete)
    db.session.commit()
    return redirect("/")


@app.route("/update/<int:sno>", methods=["GET", "POST"])
def update_task(sno):
    if request.method == "POST":
        print(request.form['title'])
        print(request.form['descc'])
        new_task = request.form['title']
        new_desc = request.form['descc']
        print(sno)
        updating_task = Todo.query.filter_by(sno =sno).first()
        updating_task.title = new_task
        updating_task.desc = new_desc
        db.session.add(updating_task)
        db.session.commit()
        return redirect("/")


     

     
    to_update = Todo.query.filter_by(sno = sno).first()
    print(to_update)
    return render_template("update.html", toUpdate = to_update)


# starting server
if __name__ == "__main__":
    # Ensure the database tables are created within the app context
    with app.app_context():
        db.create_all()  # Create database tables if they don't exist
    app.run(debug=True, port=3000)











