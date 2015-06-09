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
		data = request.get_json()
		dobList = data['dob'].split('-')
		#TODO: add all the parameters that stripe is expecting to create the account
		print stripe.Account.create(
			managed=True,
			country = data['country'],
			# first_name = data['first_name'], 
		 #    last_name = data['last_name'], 
		    # dob = {
		    #   "day": dobList[2],
		    #   "month":dobList[1],
		    #   "year": dobList[0]
		    # },
		    legal_entity = {
		    	"type":data['type'],
		    	"address" : {
		    		"line1": data['street'],
		    		"city":data['city'],
		    		"state":data['state'],
		    		"country":data['country'],
		    	}
		    },
		    
		    #ssn_last_4 = data['ssn'] 
			)

	return render_template("organizerSignup.html")


if __name__ == '__main__':
	application.run(debug=True)