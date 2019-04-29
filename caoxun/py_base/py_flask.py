# -*- encoding:utf-8 -*-

from flask import Flask
from caoxun.homework.student_managerment.model.student_managerment import StudentMgr

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello"

@app.route('/student/')
def get_all_student():
    resp = StudentMgr.student_search_all()
    return str(resp)

@app.route('/score/')
def student_score():
    return "学生成绩管理"

@app.route('/no/')
def student_no():
    num = StudentMgr.student_search_by_no('9528')
    return str(num)

@app.route('/student/tj')
def student_stat():
    tj = StudentMgr.student_stat_by_sex('nan')
    return str(tj)



if __name__ == '__main__':
    app.run(host = "0.0.0.0",port = "9566",debug = True)



