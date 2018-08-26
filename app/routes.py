from app import app
from flask import render_template, request


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_url = request.form['input_url']

    return render_template('index.html')
