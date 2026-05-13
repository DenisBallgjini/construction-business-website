from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/portfolio")
def portfolio():
    return render_template("ourwork.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":

        first_name = request.form["firstname"]
        last_name = request.form["lastname"]
        country = request.form["countryname"]
        subject = request.form["subject"]

        conn = sqlite3.connect("database/messages.db")

        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        last_name TEXT,
        country TEXT,
        subject TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        cursor.execute("""
            INSERT INTO messages
            (first_name, last_name, country, subject)

            VALUES (?, ?, ?, ?)
        """, (first_name, last_name, country, subject))

        conn.commit()
        conn.close()

        return redirect("/contact")

    return render_template("contact.html")

@app.route("/messages")
def messages():

    conn = sqlite3.connect("database/messages.db")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM messages")

    all_messages = cursor.fetchall()

    conn.close()

    return render_template(
        "messages.html",
        messages=all_messages
    )

if __name__ == "__main__":
    app.run(debug=True)