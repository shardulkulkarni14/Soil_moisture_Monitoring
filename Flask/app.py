import pyrebase
from firebase import firebase
from scapy.all import *
import random
import requests
import json
config = {
	"apiKey": "AIzaSyCe1o4Y4S3Dnhr_4PK7gA7RDNE9JY4lyts",
    "authDomain": "lp4ertos.firebaseapp.com",
    "databaseURL": "https://lp4ertos-default-rtdb.firebaseio.com",
    "projectId": "lp4ertos",
    "storageBucket": "lp4ertos.appspot.com",
    "messagingSenderId": "857766174732",
    "appId": "1:857766174732:web:e5e7f4004930b225418e29",
    # "measurementId": "G-M5YHWQQDGE"
}



FBConn = firebase.FirebaseApplication('https://lp4ertos-default-rtdb.firebaseio.com/')

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
from flask import *
import pandas as pd
app = Flask(__name__)
# app.secret_key = "hello"
db = firebase.database()

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = 'super secret key'

@app.route('/registration',methods=['GET','POST'])
def registration():
	if request.method == 'POST':
		if request.form['submit'] == 'submit':
			Fname = request.form['Fname']
			Lname = request.form['Lname']
			Country = request.form['Country']
			State = request.form['State']
			City = request.form['City']
			Pincode = request.form['Pincode']
			Pnumber = request.form['Pnumber']
			Age = request.form['Age']
			gender = request.form.get('gender')
			Addfarm = request.form['Addfarm']
			Landholding = request.form['Landholding']
			Area = request.form.get('Area')
			Passw = request.form['Passw']
			farmer = "farmer"
			data_to_upload = {
				'Name' : Fname+" "+Lname,
				'Country' : Country,
				'State' : State,
				'City' : City,
				'Pincode' : Pincode,
				'Phone Number' : Pnumber,
				'Age' : Age,
				'Gender' : gender,
				'Addfarm' : Addfarm,
				'Landholding': Landholding,
				'Area' : Area,
				'Password' : Passw
			}
			result = FBConn.post('/user_data/', data_to_upload)
			print(result)
			return redirect(url_for('login'))
	return render_template('reg-farm-index.html')





@app.route('/login',methods=['GET','POST'])
def login():
	result = FBConn.get('/user_data/',None)
	print(result)
	if request.method == 'POST':
		if request.form['submit'] == 'submit':
			email1 = request.form['Pnumber']
			session["user"] = email1
			password1 = request.form['pass']
			# cust = request.form.get('cust')
			print("hello")
			for i in result:
				a = result[i]['Phone Number']
				b = result[i]['Password']
				if email1 == a and password1 == result[i]['Password']:
					return redirect(url_for('dashboard'))
		# if request.form['submit'] == 'submit1':
		# 	return redirect(url_for('registration'))

	return render_template('login-index.html')





@app.route('/dashboard',methods=['GET','POST'])
def dashboard():
	result = FBConn.get('/user_data/',None)
	user_name =""
	name =""
	address=""
	phone=""
	if "user" in session:
		email_id = session["user"]
		print(email_id)
		for i in result:
			a = result[i]['Phone Number']
			if a ==email_id:
				name = result[i]['Name']
				address = result[i]['Addfarm']
		phone = "+91 "+a
	# result = FBConn.get('/user_data/',None)
	# user_name =""
	# name =""
	# address=""
	# phone=""
	# if "user" in session:
	# 	email_id = session["user"]
	# 	print(email_id)
	# 	for i in result:
	# 		a = result[i]['Phone Number']
	# 		if a == email_id:
	# 			name = result[i]['Name']
	# 			address = result[i]['Addfarm']
	# 	phone = "+91 "+email_id
	# data_pic = FBConn.get('/'+email_id+'/',None)
	return render_template('Dashboard.html',name=name,address=address,phone=phone)


if __name__ == '__main__':
	app.run(debug=True)