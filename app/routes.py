from flask import render_template, request, redirect, url_for
from app import app

posts = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        firstname = request.form['firstname']
        city = request.form['city']
        hobby = request.form['hobby']
        age = request.form['age']
        if firstname and city and hobby and age:
            posts.append({'firstname': firstname, 'city': city, 'hobby': hobby, 'age': age})
            return redirect(url_for('index'))
    return render_template('form.html', posts=posts)