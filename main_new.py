# coding=utf-8
import os,json,pprint
from flask import Flask, render_template,url_for, json, request, redirect, jsonify
import requests
app = Flask(__name__)

@app.route('/portal/<user>')
def portal(user):
    uri = "http://ec2-52-15-178-137.us-east-2.compute.amazonaws.com/visualization/"
    #uri = "http://172.31.65.107:8000/visualization/total_time_most_used/"
    #try:
     #   uResponse = requests.get(uri, params={"device_id": user})
    #except requests.ConnectionError:
    #    return "Connection Error"
    #Jresponse = uResponse.text
    #data = json.loads(Jresponse)
    #dataList = data['result']
    dataList = [{"label": "Testing", "value": 67}, {"label": "facebook", "value": 234234}]
    dataList = compute_hour_duration(dataList)
    print dataList
    return render_template('welcomePageUser.html' , data = dataList, user = user)

def compute_hour_duration(data):
    for i in range(len(data)):
        value_in_secs = int(data[i]["value"])
        value_in_mins = value_in_secs / 60.0
        value_in_hours = value_in_mins / 60.0
        value_in_hours = float("{0:.2f}".format(value_in_hours))
        data[i]["value"] = str(value_in_hours)
    return data

def compute_meaningful_duration(data):
    for i in range(len(data)):
        value = int(data[i]["value"])
        value_in_min = value / 60.0
        data[i]["value"] = str(value_in_min) + ' mins'
        if value_in_min > 60:
            value_in_hours = value_in_min / 60
            data[i]["value"] = str(value_in_hours) + ' hours'
            if value_in_hours > 24:
                value_in_days = value_in_hours / 24
                data[i]["value"] = str(value_in_days) + ' days'
    return data

if (__name__) == '__main__':
    app.run(debug = True)
