from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS
from config import Config
from models import init_db

app = Flask(__name__)
app.config.from_object(Config)

mysql = MySQL(app)
CORS(app)

# Initialize the database
init_db(mysql)

# Register route
@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    cursor = mysql.connection.cursor()
    cursor.execute("""
        INSERT INTO USER (name, username, password, role, email, mobile)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (data['name'], data['username'], data['password'], data['role'], data['email'], data['mobile']))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'message': 'User registered successfully'})

# Login route
@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM USER WHERE username = %s AND password = %s", 
                   (data['username'], data['password']))
    user = cursor.fetchone()
    
    if user:
        role = user[3]
        if role == 'IT_ADMIN':
            return jsonify({'role': 'IT_ADMIN'})
        else:
            return jsonify({'role': 'IT_USER_NORMAL'})
    return jsonify({'message': 'Invalid credentials'}), 401

if __name__ == '__main__':
    app.run(debug=True)
