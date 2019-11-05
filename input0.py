from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'anykey'
app.config['SQL_ALCHEMY_URI'] = 'sqlite:///firstdata.db'
db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(30), nullable=False)
	roll = db.Column(db.String(10), nullable=False, unique=True)
	hall = db.Column(db.String(30), nullable=False)

	def __repr__(self):
		return "User({}, {}, {})".format(self.name, self.roll, self.hall)

class Details(FlaskForm):
	name = StringField('name')
	roll = StringField('roll')
	hall = StringField('hall')

@app.route('/', methods=['POST', 'GET'])
def details():
	form = Details()
	user = User(name=form.name.data, roll=form.roll.data, hall=form.hall.data)
	db.session.add(user)
	db.session.commit()

	return render_template('forms.html', title='fill', form=form)
