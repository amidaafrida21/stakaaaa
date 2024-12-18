from flask import Flask, redirect, request, url_for

app = Flask(__name__)

@app.route("/login", methods=['POST'])  
def login():
    username = request.form['username']
    password = request.form['password']

    masuk = userLogin(username, password)
    if masuk:
        return redirect(url_for('dashboard'))
    else:
        return redirect(url_for('login_page'))

def userLogin(username, password):
    # Open database connection
    connection = sqlite3.connect("user.db")
    cursor = connection.cursor()
    # Execute the query
    cursor.execute("SELECT username, password FROM user WHERE username = ? AND password = ?;", 
                   (username, password))    
    count = cursor.fetchone()
    # Close the connection
    connection.close()
    return count

if __name__ == '__main__':
    print("This is flask Program!")
    app.run()
