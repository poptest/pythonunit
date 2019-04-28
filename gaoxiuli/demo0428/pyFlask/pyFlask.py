# -*- encoding:utf-8 -*-

from flask import Flask
from gaoxiuli.demo0426.student_management.model.student_management import StudentMgr
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello!"

@app.route('/student/')
def student():
    return '学员管理'

@app.route('/student/get_all_student/')
def get_all_student():
    resp = StudentMgr.student_search_all()
    return str(resp)

@app.route('/student/score/')
def score():
    return '学员成绩'

if __name__ == '__main__':
    app.run()