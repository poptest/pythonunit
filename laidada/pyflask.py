#-*- encoding:utf-8 -*-

from flask import Flask

student_list = [
    {"name": "Xiaoming", "sex": "nan", "no": "9527", "class": 1, "age": 16},
    {"name": "Xiaohong", "sex": "nv", "no": "9528", "class": 1, "age": 15},
    {"name": "Xiaobai", "sex": "nan", "no": "9529", "class": 1, "age": 16},
    {"name": "Xiaohui", "sex": "nv", "no": "9530", "class": 1, "age": 16}
]

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello"

@app.route('/student')
def gei_all_student():
    return str(student_list)

@app.route('/score')
def score():
    return "成绩管理"

if __name__ == '__main__':
    app.run(host="0.0.0.0",port="0536",debug=True)