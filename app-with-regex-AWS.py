from flask import Flask, render_template, request
import mysql.connector, random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    myName = ''
    myMobile = ''
    message = ''

    # Predefined random values
    random_names = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
    random_numbers = ['03001234567', '03111234567', '03211234567', '03331234567', '03451234567']

    if request.method == 'POST':
        myName = request.form.get('name', '').strip()
        myMobile = request.form.get('mobile', '').strip()

        # If no input, use random ones
        if not myName:
            myName = random.choice(random_names)
        if not myMobile:
            myMobile = random.choice(random_numbers)

        insert_data(myName, myMobile)
        message = 'Form submitted successfully with random values' if not request.form['name'] else 'Form submitted successfully'

    return render_template('index.html', name=myName, mobile=myMobile, message=message)

def insert_data(myName, myMobile):
    
    connection = connect_to_database()
    print(f" inside the insert db method on AWS")
    if connection is not None:
        cursor = connection.cursor()
        try:
            print(f" inside the insert try ")
            print(f"value for name: {myName}")
            print(f"value for name: {myMobile}")
            cursor.execute("INSERT INTO users (name, mobile) VALUES (?, ?)", (myName, myMobile))
            connection.commit()
            last_row_id = cursor.lastrowid  # Get the ID of the last inserted row
            print(f"Inserted data with ID: {last_row_id}")
        except sqlite3.Error as e:
            print("Error inserting data:", e)
        finally:
            connection.close()
    else:
        print("Cannot perform database operations because the connection failed")

def select_all_data():
    connection = connect_to_database()
    if connection is not None:
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM users")
            rows = cursor.fetchall()
            return rows
        except sqlite3.Error as e:
            print("Error selecting data:", e)
        finally:
            connection.close()
    else:
        print("Cannot perform database operations because the connection failed")
        return None


def create_table():
    try:
        conn = sqlite3.connect('myTestDb.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users
                          (id INTEGER PRIMARY KEY, name TEXT, mobile TEXT)''')
        conn.commit()
        conn.close()
        print("Table created successfully on AWS")
    except sqlite3.Error as e:
        print("Error creating table on AWS:", e)

def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host="database-1.cls68qui4ttx.eu-north-1.rds.amazonaws.com",  # Replace with your RDS endpoint
            user="admin",
            password="Password#1",
            database="myflaskdb"
        )
        print("Connected to RDS MySQL!")
        return conn
    except mysql.connector.Error as e:
        print("Error connecting to RDS:", e)
        return None

@app.route('/save/<name>') ### passing a parameter that will help entering the name from the url 
def save(name):
   
    print('inside the save method for AWS')
    return render_template('user.html' , name=name) ### creating a simple route that takes input from the user via address bar 

@app.route('/user') ## render template example to give names without id's
def user():
    first_name="Nouman"
    last_name="zahid"
    stuff="<strong>this is a stuff text<strong>"
    favorite_pizza=["cheese","pepperoni","supreme"]
    return render_template('user.html',first_name=first_name,name=last_name,stuff=stuff,
    favorite_pizza=favorite_pizza)## change to striptags to check another functionality
if __name__ == '__main__':
    create_table()
    debug_mode = os.environ.get('FLASK_DEBUG', 'False') == 'True'
    app.run(host='0.0.0.0', port=5000, debug=debug_mode) 
