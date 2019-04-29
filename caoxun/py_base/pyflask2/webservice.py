# -*- encoding:utf-8 -*-

from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/factory/add",methods=['GET','POST'])
def factory_add():
    req_method = request.method
    print("User Request Method:%s" % req_method)
    if req_method == 'GET':
        return render_template("factory_add.html")
    else:
        no = "0001"
        name = request.form.get("fac_name")
        city = request.form.get("city")
        address = request.form.get("address")
        contact = request.form.get("contact")
        tel = request.form.get("tel")
        dj = request.form.get("dj")
        status = "1"

        return render_template("factory_add_success.html",
                               no = no,
                               name = name,
                               city = city,
                               address = address,
                               contact = contact,
                               tel = tel,
                               dj = dj,
                               status = status
                               )





if __name__ == '__main__':
    app.run()
