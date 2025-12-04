from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os

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
    phone_number = request.form['phone_number']
    phone_list = request.form['phone']
    medical_assistance = request.form['medical_assistance']
    medical_box = request.form['medical_box']
    extra_box = request.form['extra_box']

    if os.path.exists('registrations.json'):
        with open('registrations.json', 'r') as file:
            data = json.load(file)

    else:
        data = []

    data.append({'name': name, 'last_name': last_name, 'birth_date': birth_date, 'email': email, 'phone_number': phone_number, 'phone_list': phone_list, 'medical_assistance': medical_assistance, 'medical_box': medical_box, 'extra_box': extra_box})
    with open('registrations.json', 'w') as file:
        json.dump(data, file, indent=2)
    return redirect(url_for('index'))

    if not name or not last_name or not birth_date or not email or not phone_number or not phone_list:
        flash('all fields are required to be filled in!')
        return redirect(url_for('register'))
    else:
        print(f"Thank you {name}, your contact information has been saved!.")
        return f"Thank you {name}, your contact information has been saved!."





@app.route('/register')
def register():
    return render_template("register.html")


@app.route('/view')
def view_registrations():
    if os.path.exists('view.html'):
        data = [...]
        return render_template('view.html', registrations=data)
    else:
        data = []
        return render_template('view.html', registrations=data)



if __name__ == '__main__':
    app.run(debug=True)