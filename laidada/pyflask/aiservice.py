# -*- encoding:utf-8 -*-

from flask import Flask,request
app = Flask(__name__)

@app.route('/factory/add', methods=['GET','POST'])
def factory_add():
    print(request.method)
    if request.method =='GET':
        html_page = '''
            <form actiong=""method="post">
                工厂名称：<input name="name" type="text"/>
                城市：<input name="city" type="text"/>
                <input type="submit">
            </form>
        '''
        return (html_page)
    else:
        name = request.form.get('name')
        city = request.form.get('city')
        resp_msg ="%s %s"%(name,city)
        return (resp_msg)

if __name__ == '__main__':
    app.run()
