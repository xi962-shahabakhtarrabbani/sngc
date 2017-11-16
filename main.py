# coding=utf-8
import os,json,pprint
from flask import Flask, render_template,url_for, json, request, redirect, jsonify
import requests
app = Flask(__name__)

# Miscellaneous functions
def compute_hour_duration(data):
    for i in range(len(data)):
        value_in_secs = int(data[i]["value"])
        value_in_mins = value_in_secs / 60.0
        value_in_hours = value_in_mins / 60.0
        value_in_hours = float("{0:.2f}".format(value_in_hours))
        data[i]["value"] = str(value_in_hours)
    return data


@app.route('/userPortal/<user>')
def userPortal(user):
    uri1="http://ec2-52-15-178-137.us-east-2.compute.amazonaws.com/visualization/current_date"
    uri2="http://ec2-52-15-178-137.us-east-2.compute.amazonaws.com/visualization/total_time_most_used"
    uri3="http://ec2-52-15-178-137.us-east-2.compute.amazonaws.com/visualization/weekly_time_used"
    uri4="http://ec2-52-15-178-137.us-east-2.compute.amazonaws.com/visualization/most_used"
    uri5="http://ec2-52-15-178-137.us-east-2.compute.amazonaws.com/visualization/least_used"


    # Daily Usage
    try:
        uResponse = requests.get(uri1,params={"device_id":user})
    except requests.ConnectionError:
        return "Connection Error"
    Jresponse = uResponse.text
    data1 = json.loads(Jresponse)
    dataList1=data1['result']
    dataList1 = compute_hour_duration(dataList1)

    for app in dataList1:
        try:
            index=app['label'].rfind('.')
            app['label']=app['label'][index+1:].title()
            pass
        except:
            pass


    # Most used
    try:
        uResponse = requests.get(uri2,params={"device_id":user})
    except requests.ConnectionError:
        return "Connection Error"
    Jresponse = uResponse.text
    data2 = json.loads(Jresponse)
    dataList2=data2['result']
    dataList2 = compute_hour_duration(dataList2)

    for app in dataList2:
        try:
            index=app['label'].rfind('.')
            app['label']=app['label'][index+1:].title()
            pass
        except:
            pass


    # Weekly data
    try:
        uResponse = requests.get(uri3,params={"device_id":user})
    except requests.ConnectionError:
        return "Connection Error"
    Jresponse = uResponse.text
    data3 = json.loads(Jresponse)
    dataList3=data3['result']
    # dataList3 = compute_hour_duration(dataList3)
    weekData=[]

    appList=[]

    for key, value in dataList3.iteritems():
        for app in value:
            if app['app_name'] not in appList:
                index = app['app_name'].rfind('.')
                appList.append(app['app_name'][index+1:].title())
            else:
                pass

    for app in appList:
        appDict={}
        appDict['seriesname']=app
        appDict['data']=[{'value':'0'},{'value':'0'},{'value':'0'},{'value':'0'}]


        for key, value in dataList3.iteritems():
            pos=int(key[-1])

            for appName in value:
                index = appName['app_name'].rfind('.')
                if appName['app_name'][index+1:].title()==app:
                    appDict['data'][pos-1]['value']=str(appName['duration'])
                    pass


        weekData.append(appDict)

    # Most used app
    try:
        uResponse = requests.get(uri4,params={"device_id":user})
    except requests.ConnectionError:
        return "Connection Error"
    Jresponse = uResponse.text
    data4 = json.loads(Jresponse)
    dataList4=data4['result']
    # dataList4 = compute_hour_duration(dataList4)
    index1 = dataList4['label'].rfind('.')
    dataList4['label']=dataList4['label'][index1+1:].title()

    # Least used app
    # try:
    #     uResponse = requests.get(uri5, params={"device_id": user})
    # except requests.ConnectionError:
    #     return "Connection Error"
    # Jresponse = uResponse.text
    # data5 = json.loads(Jresponse)
    # dataList5 = data5['result']
    # # dataList5 = compute_hour_duration(dataList5)

    pass



    return render_template('welcomePageUser.html',data1=dataList1,data2=dataList2,data3=weekData,mostUsed=dataList4,user=user)


@app.route('/adminPortal/<user>')
def adminPortal(user):
    uri1 = "http://ec2-52-15-178-137.us-east-2.compute.amazonaws.com/visualization/last7_days"
    uri2 = "http://ec2-52-15-178-137.us-east-2.compute.amazonaws.com/visualization/max_used_all"
    uri3 = "http://ec2-52-15-178-137.us-east-2.compute.amazonaws.com/visualization/min_used_all"

    # Last 7 days
    try:
        uResponse = requests.get(uri1, params={"device_id": user})
    except requests.ConnectionError:
        return "Connection Error"
    Jresponse = uResponse.text
    data1 = json.loads(Jresponse)
    dataList1 = data1['result']
    dataList1 = compute_hour_duration(dataList1)

    return render_template('adminPortal.html',user=user)


@app.route('/')
def landingPage():
    return render_template('landingPage2.html')



@app.route('/userLogin',methods=['GET', 'POST'])
def userLogin():
    if request.method == 'POST':

        username=request.form['username']
        # send these to the server

        return redirect(url_for('userPortal',user=username))

    return render_template('userLogin.html')

@app.route('/adminLogin',methods=['GET', 'POST'])
def adminLogin():
    if request.method == 'POST':

        username=request.form['username']
        # send these to the server

        return redirect(url_for('adminPortal',user=username))

    return render_template('adminLogin.html')




if __name__ == '__main__':
   app.run(debug = True)