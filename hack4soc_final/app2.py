""" from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

# Replace these placeholders with your MySQL server details
host = "localhost"
user = "root"
password = "Home@5095"
database = "information"

userdata_config = {
    'host': host,
    'user': user,
    'password': password,
    'database': database
}

checkdata_config = {
    'host': host,
    'user': user,
    'password': password,
    'database': database
}

def compare_passwords():
    try:
        # Connect to the userdata database
        userdata_conn = mysql.connector.connect(**userdata_config)
        userdata_cursor = userdata_conn.cursor()

        # Connect to the checkdata database
        checkdata_conn = mysql.connector.connect(**checkdata_config)
        checkdata_cursor = checkdata_conn.cursor()

        # Fetch email and password from userdata
        userdata_cursor.execute("SELECT email, password FROM userdata")
        userdata_results = userdata_cursor.fetchall()

        for email, password_userdata in userdata_results:
            # Fetch password from checkdata for the same email
            checkdata_cursor.execute("SELECT password FROM checkdata WHERE email = %s", (email,))
            checkdata_result = checkdata_cursor.fetchone()

            if checkdata_result:
                password_checkdata = checkdata_result[0]

                # Compare passwords
                if password_userdata == password_checkdata:
                    print(f"Passwords match for email: {email}")
                else:
                    print(f"Passwords do not match for email: {email}")
            else:
                print(f"No entry found in checkdata for email: {email}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close database connections
        if userdata_conn.is_connected():
            userdata_cursor.close()
            userdata_conn.close()

        if checkdata_conn.is_connected():
            checkdata_cursor.close()
            checkdata_conn.close()

@app.route("/")
def index():
    return render_template("index2.html")

@app.route("/submit_data", methods=["POST"])
def submit_data():
    try:
        # Parse JSON data from the request
        data = request.get_json()

        # Connect to MySQL
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Insert data into the 'userdata' table
        insert_query = "INSERT INTO checkdata (email,password) VALUES (%s, %s)"
        data_values = (data['email'], data['password'])
        cursor.execute(insert_query, data_values)

        # Commit the changes
        connection.commit()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        return jsonify({"message": "Data submitted successfully!"})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True) """


from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

# Replace these placeholders with your MySQL server details
host = "localhost"
user = "root"
password = "Home@5095"
database = "information"

userdata_config = {
    'host': host,
    'user': user,
    'password': password,
    'database': database
}

checkdata_config = {
    'host': host,
    'user': user,
    'password': password,
    'database': database
}

def compare_passwords():
    try:
        # Connect to the userdata database
        userdata_conn = mysql.connector.connect(**userdata_config)
        userdata_cursor = userdata_conn.cursor()

        # Connect to the checkdata database
        checkdata_conn = mysql.connector.connect(**checkdata_config)
        checkdata_cursor = checkdata_conn.cursor()

        # Fetch email and password from userdata
        userdata_cursor.execute("SELECT email, password FROM userdata")
        userdata_results = userdata_cursor.fetchall()

        for email, password_userdata in userdata_results:
            # Fetch password from checkdata for the same email
            checkdata_cursor.execute("SELECT password FROM checkdata WHERE email = %s", (email,))
            checkdata_result = checkdata_cursor.fetchone()

            if checkdata_result:
                password_checkdata = checkdata_result[0]

                # Compare passwords
                if password_userdata == password_checkdata:
                    return f"Passwords match for email: {email}"
                else:
                    return f"Passwords do not match for email: {email}.Please try again."
            else:
                return f"No entry found in checkdata for email: {email}"

    except Exception as e:
        return f"Error: {e}"

    finally:
        # Close database connections
        if userdata_conn.is_connected():
            userdata_cursor.close()
            userdata_conn.close()

        if checkdata_conn.is_connected():
            checkdata_cursor.close()
            checkdata_conn.close()

@app.route("/")
def index():
    return render_template("index2.html")

@app.route("/submit_data", methods=["POST"])
def submit_data():
    try:
        # Parse JSON data from the request
        data = request.get_json()

        # Connect to MySQL
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Insert data into the 'userdata' table
        insert_query = "INSERT INTO checkdata (email, password) VALUES (%s, %s)"
        data_values = (data['email'], data['password'])
        cursor.execute(insert_query, data_values)

        # Commit the changes
        connection.commit()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        # Compare passwords
        match_message = compare_passwords()
        return jsonify({"message": "Data submitted successfully!", "match_message": match_message})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)

















""" from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

# Replace these placeholders with your MySQL server details
host = "localhost"
user = "root"
password = "Home@5095"
database = "information"

userdata_config = {
    'host': host,
    'user': user,
    'password': password,
    'database': database
}

checkdata_config = {
    'host': host,
    'user': user,
    'password': password,
    'database': database
}

def compare_passwords():
    try:
        # Connect to the userdata database
        userdata_conn = mysql.connector.connect(**userdata_config)
        userdata_cursor = userdata_conn.cursor()

        # Connect to the checkdata database
        checkdata_conn = mysql.connector.connect(**checkdata_config)
        checkdata_cursor = checkdata_conn.cursor()

        # Fetch email and password from userdata
        userdata_cursor.execute("SELECT email, password FROM userdata")
        userdata_results = userdata_cursor.fetchall()

        for email, password_userdata in userdata_results:
            # Fetch password from checkdata for the same email
            checkdata_cursor.execute("SELECT password FROM checkdata WHERE email = %s", (email,))
            checkdata_result = checkdata_cursor.fetchone()

            if checkdata_result:
                password_checkdata = checkdata_result[0]

                # Compare passwords
                if password_userdata == password_checkdata:
                    print(f"Passwords match for email: {email}")
                else:
                    print(f"Passwords do not match for email: {email}")
            else:
                print(f"No entry found in checkdata for email: {email}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Close database connections
        if userdata_conn.is_connected():
            userdata_cursor.close()
            userdata_conn.close()

        if checkdata_conn.is_connected():
            checkdata_cursor.close()
            checkdata_conn.close()

@app.route("/")
def index():
    return render_template("index2.html")

@app.route("/submit_data", methods=["POST"])
def submit_data():
    try:
        # Parse JSON data from the request
        data = request.get_json()

        # Connect to MySQL
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Insert data into the 'userdata' table
        insert_query = "INSERT INTO checkdata (email, password) VALUES (%s, %s, %s)"
        data_values = (data['email'], data['password'])
        cursor.execute(insert_query, data_values)

        # Commit the changes
        connection.commit()

        # Close the cursor and connection
        cursor.close()
        connection.close()

        # Compare passwords
        compare_passwords()

        return jsonify({"message": "Data submitted successfully!"})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True) """
