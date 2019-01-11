#!/usr/bin/env python3
from flask import Flask, render_template, request, make_response

from csp import csp

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@csp
def home(inline_script_nonce):
    context = {
        'css_class': 'class1',
        'additional_script': None,
        'inline_script_nonce': inline_script_nonce
    }
    if request.method == 'POST':
        if request.form['css_class']:
            context['css_class'] = request.form['css_class']
        if request.form['additional_script']:
            context['additional_script'] = request.form['additional_script']
    return render_template('home.html', **context)


@app.route('/report-csp-violations', methods=['POST'])
def report():
    print(request.data)
    response = make_response()
    response.status_code = 200
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0')
