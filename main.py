# coding=utf-8
import os
from flask import Flask, render_template,url_for, json, request, redirect, jsonify
import requests
app = Flask(__name__)

@app.route('/portal/<user>')
def portal(user):
    # filename = os.path.join(app.static_folder, 'data/appUptime.json')
    # with open(filename) as blog_file:
    #     data = json.load(blog_file)



    # uri="http://ec2-52-15-178-137.us-east-2.compute.amazonaws.com/visualization/"
    uri="http://172.31.75.213:8000/visualization"
    try:
        uResponse = requests.get(uri,params={"key":user})
    except requests.ConnectionError:
        return "Connection Error"
    Jresponse = uResponse.text
    data = json.loads(Jresponse)
    dataList=data['data']
    return render_template('welcome.html',data=dataList,user=user)


@app.route('/')
def landingPage():
    return render_template('landingPage.html')

@app.route('/login',methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        username=request.form['username']
        # send these to the server

        return redirect(url_for('portal',user=username))

    return render_template('login.html')



if __name__ == '__main__':
   app.run(debug = True)