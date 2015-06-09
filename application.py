import os
import stripe
from flask import Flask, render_template, request
from datetime import date


stripe_keys = {
	'secret_key': os.environ['SECRET_KEY'],
	'publishable_key': os.environ['PUBLISHABLE_KEY']
}

stripe.api_key= stripe_keys['secret_key']

application = Flask(__name__)

@application.route('/')
def index():
	return render_template("index.html",key=stripe_keys['publishable_key'])

@application.route('/charge',methods=['POST'])
def charge():
	amnt = 500
	customer = stripe.Customer.create(
		email = "coolchanteur@gmail.com",
		card = request.form['stripeToken']
	)

	charge = stripe.Charge.create(
		customer = customer.id,
		amount = amnt,
		currency='usd',
		description='Codo Charge'

	)

	return render_template("charge.html",amount=amnt)

@application.route("/organizer_signup", methods=['GET','POST'])
def organizer_signup():
	if request.method == 'POST':
		print type(request.form)
		data = dict(request.form)
		#TODO: add all the parameters that stripe is expecting to create the account
		print stripe.Account.create(
			managed=True,
			country = data.get('country'),
			first_name = data.get('first_name'), 
		    last_name = data.get('last_name'), 
		    dob = data.get('dob'),
		    type = data.get('type'),
		    sss_last_4 = data.get('ssn'), 
		   
			)

	return render_template("organizerSignup.html")


if __name__ == '__main__':
	application.run(debug=True)