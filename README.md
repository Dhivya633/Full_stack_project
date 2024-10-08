# Full_stack_project
NAME:DHIVYADHARSHINI
Company Management Application
Technologies Used:
-	Backend: Flask (Python)
-	Frontend: React (JavaScript)
-	Database: MySQL
Setup Instructions:
Backend (Python + Flask)
1.	Install required packages:
pip install Flask flask-mysqldb
2.	Setup for React:
npx create-react-app frontend cd frontend
npm start
CODE:

1.	Database Setup:

Used MySQL WorkBench to create the necessary tables: USER and COMPANY. CREATE TABLE USER (
id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100),
username VARCHAR(100), password VARCHAR(100), role VARCHAR(20),
email VARCHAR(100),

mobile VARCHAR(15)
 
);



CREATE TABLE COMPANY (

id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100),
address VARCHAR(255), created_by VARCHAR(100),
status ENUM('approved', 'unapproved')
);

2.	Backend (Python + Flask)

Created a Flask app to handle the backend logic.
from flask import Flask, request, jsonify import MySQLdb


app = Flask(  name  )



# Connect to MySQL

db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="company_db")



@app.route('/register', methods=['POST']) def register():
data = request.json cursor = db.cursor()
 
query = "INSERT INTO USER (name, username, password, role, email, mobile) VALUES (%s, %s, %s, %s, %s, %s)"

cursor.execute(query, (data['name'], data['username'], data['password'], data['role'], data['email'], data['mobile']))

db.commit()

return jsonify({'message': 'User registered successfully!'})



@app.route('/login', methods=['POST']) def login():
data = request.json cursor = db.cursor()
query = "SELECT * FROM USER WHERE username=%s AND password=%s" cursor.execute(query, (data['username'], data['password']))
user = cursor.fetchone() if user:
if user[3] == 'IT_ADMIN':
return jsonify({'message': 'Admin logged in', 'role': 'admin'}) else:
return jsonify({'message': 'User logged in', 'role': 'user'}) return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/company', methods=['POST']) def create_company():
data = request.json
 
cursor = db.cursor()

query = "INSERT INTO COMPANY (name, address, created_by, status) VALUES (%s, %s,
%s, %s)"

status = 'approved' if data['role'] == 'IT_ADMIN' else 'unapproved' cursor.execute(query, (data['name'], data['address'], data['created_by'], status)) db.commit()
return jsonify({'message': 'Company created successfully!'})



if  name	== ' main ': app.run(debug=True)
3.	Frontend (React):

Created React components to handle the register, login, and company creation screens. import React, { useState } from 'react';


const Register = () => {

const [formData, setFormData] = useState({ name: '',
username: '',

password: '',

role: 'IT_USER_NORMAL', // default role email: '',
mobile: ''

});
 
const handleChange = (e) => { setFormData({
...formData,

[e.target.name]: e.target.value

});

};



const handleSubmit = async (e) => { e.preventDefault();
const response = await fetch('http://localhost:5000/register', { method: 'POST',
headers: {

'Content-Type': 'application/json'

},

body: JSON.stringify(formData)

});

const result = await response.json(); alert(result.message);
};



return (

<form onSubmit={handleSubmit}>

<input name="name" placeholder="Name" onChange={handleChange} />
 
<input name="username" placeholder="Username" onChange={handleChange} />

<input name="password" type="password" placeholder="Password" onChange={handleChange} />

<input name="email" placeholder="Email" onChange={handleChange} />

<input name="mobile" placeholder="Mobile" onChange={handleChange} />

<select name="role" onChange={handleChange}>

<option value="IT_USER_NORMAL">Normal User</option>

<option value="IT_ADMIN">Admin</option>

</select>

<button type="submit">Register</button>

</form>

);

};

4.	Running the Project

Start Flask Backend:Open a terminal, navigate to the backend folder and run: python app.py
Start React Frontend: Open a separate terminal, navigate to the frontend folder, and run:

npm start


#OUTPUT:
1.	REGISTER PAGE:
ADMIN USER:
 NORMAL USER-1:
 NORMAL USER-2:
 Normal User-3: 
2.	LOGIN PAGE: 
3.	Admin Screen for Company Listing:
4.	Normal User Screen for Company Listing:

