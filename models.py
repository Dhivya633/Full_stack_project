from flask_mysqldb import MySQL

def init_db(mysql):
    cursor = mysql.connection.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS USER (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            username VARCHAR(255) UNIQUE,
            password VARCHAR(255),
            role ENUM('IT_ADMIN', 'IT_USER_NORMAL'),
            email VARCHAR(255),
            mobile VARCHAR(20)
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS COMPANY (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            address VARCHAR(255),
            created_by INT,
            status ENUM('approved', 'unapproved') DEFAULT 'unapproved',
            FOREIGN KEY (created_by) REFERENCES USER(id)
        )
    """)
    
    mysql.connection.commit()
    cursor.close()
