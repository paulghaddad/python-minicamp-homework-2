from flask import Flask, render_template, jsonify
from datetime import datetime, date

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/birthday')
def my_birthday():
    birthday = date(1982, 10, 16)
    return birthday.strftime('%B %d %Y')

@app.route('/greeting/<name>')
def greeting(name):
    return 'Hello %s!' % name.capitalize()

@app.route('/add/<int:num_1>/<int:num_2>')
def add(num_1, num_2):
    sum = num_1 + num_2
    return '%d' % sum

@app.route('/subtract/<int:num_1>/<int:num_2>')
def subtract(num_1, num_2):
    difference = num_1 - num_2
    return '%d' % difference

@app.route('/multiply/<int:num_1>/<int:num_2>')
def multiply(num_1, num_2):
    product = num_1 * num_2
    return '%d' % product

@app.route('/favoritefoods')
def favoritefoods():
    my_favorite_foods = ['pizza', 'spaghetti', 'salmon']
    formatted_foods = list(map(lambda food: food.capitalize(), my_favorite_foods))
    return jsonify(formatted_foods)
