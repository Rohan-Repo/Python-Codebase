# Create virtual env : python -m venv venv
# Activate Virtual Env : .\venv\Scripts\activate
# Install Flask : pip install flask
# Run as : python .\MyApp.py
# Navigate to http://localhost:5000/


from flask import Flask, render_template
import sqlite3

myApp = Flask(__name__)

def get_db_data():
    # Complete Path to your SQLite DB 
    conn = sqlite3.connect('Product.db')
    cursor = conn.cursor()

    cursor.execute( 'SELECT productName, productType, productPrice, orderQuantity, productPrice * orderQuantity AS totalAmount FROM Products INNER JOIN Orders ON Products.productID = Orders.productID' )
    data = cursor.fetchall()

    conn.close()

    return data

@myApp.route('/')
def index():
    data = get_db_data()
    return render_template( 'index.html', data=data )

if __name__ == '__main__':
    myApp.run( debug=True )