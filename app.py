from flask import Flask, render_template, request, redirect, url_for
import os
from flask_sqlalchemy import SQLAlchemy
from forms import LookUpForm
import dotenv

dotenv.load_dotenv()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///myDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')
db= SQLAlchemy(app)


class phone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(15), index=True, unique=True)
    name= db.Column(db.String(100), index=True, unique=False)



    def __repr__(self):
        return f"Phone number: {self.number} Name: {self.name}"


@app.route('/', methods=["GET", "POST"])
@app.route('/home', methods=["GET", "POST"])
def lookup_number():
    form = LookUpForm(csrf_enabled=False)
    if form.validate_on_submit():
        number = form.number.data
        phone_number = phone.query.filter_by(number=number).first()
        if phone_number:
            return redirect(url_for('patient_info', number=number))
    return render_template('lookup.html', form=form)

@app.route('/<number>')
def patient_info(number):
    phone_number = phone.query.filter_by(number=number).first_or_404()
    return render_template('patient_info.html', phone_number=phone_number)


@app.route('/add_test_data')
def add_test_data():
    sophia = phone(number='9047725804', name='Sophia')
    susan = phone(number='9047076887', name='Susan')

    db.session.add(sophia)
    db.session.add(susan)
    db.session.commit()

    return "Test data added!"


if __name__ == '__main__':
    app.run()
