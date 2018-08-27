from app import app
from flask import render_template, request
from .models import URL


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_url = request.form['input_url']
        a = URL().launch_task(input_url)
        print(a)

    return render_template('index.html')
