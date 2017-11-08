# coding=utf-8
import os,json,pprint
from flask import Flask, render_template,url_for, json, request, redirect, jsonify
import requests
app = Flask(__name__)

@app.route('/portal/<user>')
def portal(user):
    # filename = os.path.join(app.static_folder, 'data/'+user+'.json')
    # with open(filename) as blog_file:
    #     dataList = json.load(blog_file)

    uri="http://ec2-52-15-178-137.us-east-2.compute.amazonaws.com/visualization/"
    # uri="http://172.31.75.213:8000/visualization"
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
    totalData=[{"value": "0", "label": "Whatsapp"}, {"value": "0", "label": "Facebook"}, {"value": "0", "label": "Instagram"}, {"value": "0", "label": "Zomato"}, {"value": "0", "label": "Quora"}, {"value": "0", "label": "Camera"}, {"value": "0", "label": "Notes"}, {"value": "0", "label": "Ola"}, {"value": "0", "label": "Uber"}]

    avgData=[{"value": "0", "label": "Whatsapp"}, {"value": "0", "label": "Facebook"}, {"value": "0", "label": "Instagram"}, {"value": "0", "label": "Zomato"}, {"value": "0", "label": "Quora"}, {"value": "0", "label": "Camera"}, {"value": "0", "label": "Notes"}, {"value": "0", "label": "Ola"}, {"value": "0", "label": "Uber"}]

    for i in range(20):
        filename = os.path.join(app.static_folder, 'data/user'+str(i)+'.json')
        with open(filename) as data_file:
            data = json.load(data_file)
            for j in range(len(data)):
                value=int(data[j]["value"])
                totalData[j]["value"]=str(int(totalData[j]["value"])+value)

    for i in range(len(totalData)):
        avgData[i]["value"]=int(totalData[i]["value"])/20


    return render_template('landingPage2.html',avgData=avgData,totalData=totalData)

@app.route('/login',methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        username=request.form['username']
        # send these to the server

        return redirect(url_for('portal',user=username))

    return render_template('login.html')



if __name__ == '__main__':
   app.run(debug = True)