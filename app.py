from flask import Flask, render_template, request, flash
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        # Here you would typically send an email or save to database
        flash('Thank you for your message! We will get back to you soon.')
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True) 