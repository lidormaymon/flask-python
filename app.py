from flask import Flask,render_template
from enum import Enum


app = Flask(__name__)


class Cars(Enum):
    FERRARI = 1
    LAMBO = 2
    MCLAREN = 3


@app.route('/')
def home():
    car_list = [car.name for car in Cars]
    return render_template('index.html', cars =car_list)

@app.route("/gallery")
def gallery():
    return render_template('gallery.html')

if __name__ == '__main__':
    app.run(debug=True)

