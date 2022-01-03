from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hello.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    surname = db.Column(db.String)
    email = db.Column(db.String)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        email = request.form['email']
        person = Person(name=name, surname=surname, email=email)
        exists = db.session.query(Person).filter_by(name=name).scalar() is not None
        if exists:
            person = Person.query.filter_by(name=name).first()
            return render_template('already_seen_you.html', name=person.name)
        else:
            db.session.add(person)
            db.session.commit()
            return render_template('/nice_to_meet_you.html', name=name, surname=surname)
    else:
        return render_template('index.html')


@app.route('/show_all')
def show_all():
    persons = Person.query.order_by(Person.name.desc()).all()
    return render_template("persons.html", persons=persons)


@app.route('/person/<int:id>/delete')
def post_delete(id):
    person = Person.query.get_or_404(id)
    try:
        db.session.delete(person)
        db.session.commit()
        return redirect('/')
    except:
        return 'The error occurred while deleting post'


if __name__ == '__main__':
    app.run(debug=True)
