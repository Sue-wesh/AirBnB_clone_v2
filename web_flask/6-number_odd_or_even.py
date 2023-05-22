#!/usr/bin/python3
""" start a flask web application"""
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """display hello hbnb"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """display hbnb"""
    return 'HBNB'


@app.route('/c/<text>')
def C_var(text):
    """display C followed by the value of the text variable"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/(<text>)')
def Python_is_cool(text='is cool'):
    """display python followed by value of text variable"""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number(n):
    """n is only an integer"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """display html page only if n is int"""
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>')
def odd_even(n):
    """n is odd or even"""
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
