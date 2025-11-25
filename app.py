from flask import Flask, render_template, request, redirect, url_for, flash
import re

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['first_name']
    last_name = request.form['last_name']
    birth_date = request.form['birth_date']
    email = request.form['email']
    if not name or not last_name or not birth_date or not email:
        flash('all fields are required to be filled in!')
        return redirect(url_for('register'))
    else:
        print(f"Thank you {name}, your contact information has been saved!.")
        return f"Thank you {name}, your contact information has been saved!."

@app.route('/register')
def register():
    return render_template("register.html")





if __name__ == '__main__':
    app.run(debug=True)