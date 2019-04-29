# -*- encoding:utf-8 -*-
from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/factory/add",methods=['POST','GET'])
def factory_add():
    req_method = request.method
    print("User Request method: %s " % req_method)
    if req_method == 'GET':
        return render_template("factory.html")
    else:
        no = "001"
        name = request.form.get("fact_name")
        city = request.form.get("city")
        address = request.form.get("address")
        contact = request.form.get("contact")
        tel = request.form.get("tel")
        DJ = request.form.get("DJ")
        contact = request.form.get("contact")
        return render_template("factory_add.html",
                               no=no,
                               name=name,
                               city=city,
                                address=address,
                               contact=contact,
                               tel=tel,
                               DJ=DJ,
                            )

if __name__ == '__main__':
    app.run()