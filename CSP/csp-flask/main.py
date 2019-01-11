#!/usr/bin/env python3
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    context = {
        'css_class': 'class1',
        'additional_script': None
    }
    if request.method == 'POST':
        if request.form['css_class']:
            context['css_class'] = request.form['css_class']
        if request.form['additional_script']:
            context['additional_script'] = request.form['additional_script']
    return render_template('home.html', **context)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
