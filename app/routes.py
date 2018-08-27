from app import app
from flask import render_template, request
from .models import URL


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_url = request.form['input_url']
        URL().launch_task('save_url', 'crawling for '+str(input_url))

    return render_template('index.html')
