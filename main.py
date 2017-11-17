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
        data[i]["value"] = str(value_in_mins)
    return data

def convert2minutes(data):
    return str(int(data)/60.0)


@app.route('/userPortal/<user>')
def userPortal(user):
    uri1="http://ec2-52-15-178-137.us-east-2.compute.amazonaws.com/visualization/current_date"
    uri2="http://ec2-52-15-178-137.us-east-2.compute.amazonaws.com/visualization/total_time_most_used_10apps"
    uri3="http://ec2-52-15-178-137.us-east-2.compute.amazonaws.com/visualization/weekly_time_used"
    uri4="http://ec2-52-15-178-137.us-east-2.compute.amazonaws.com/visualization/most_used"
    uri5="http://ec2-52-15-178-137.us-east-2.compute.amazonaws.com/visualization/least_used"
    uri6 = "http://ec2-52-15-178-137.us-east-2.compute.amazonaws.com/visualization/last7_days"

    # Daily Usage
    try:
        uResponse = requests.get(uri1,params={"device_id":user})
    except requests.ConnectionError:
        return "Connection Error"
    Jresponse = uResponse.text
    data1 = json.loads(Jresponse)
    dataList1=data1['result']
    # try:
    #     dataList1 = compute_hour_duration(dataList1)
    # except:
    #     pass

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
    # try:
    #     dataList2 = compute_hour_duration(dataList2)
    # except:
    #     pass

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

    for app in weekData:
        for data1 in app['data']:
            data1['value']=convert2minutes(data1['value'])




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
    try:
        uResponse = requests.get(uri5, params={"device_id": user})
    except requests.ConnectionError:
        return "Connection Error"
    Jresponse = uResponse.text
    data5 = json.loads(Jresponse)
    dataList5 = data5['result']
    index1 = dataList5['label'].rfind('.')
    dataList5['label'] = dataList5['label'][index1 + 1:].title()
    # dataList5 = compute_hour_duration(dataList5)



    # Last 7 days
    try:
        uResponse = requests.get(uri6, params={"device_id": user})
    except requests.ConnectionError:
        return "Connection Error"
    Jresponse = uResponse.text
    data6 = json.loads(Jresponse)
    dataList6 = data6['result']
    # try:
    #     dataList1 = compute_hour_duration(dataList6)
    # except:
    #     pass

    for app in dataList6:
        try:
            index = app['label'].rfind('.')
            app['label'] = app['label'][index + 1:].title()
            pass
        except:
            pass

    dataList6=compute_hour_duration(dataList6)


    return render_template('welcomePageUser.html',data1=dataList1,data2=dataList2,data3=weekData,mostUsed=dataList4,leastUsed=dataList5,last7=dataList6,user=user)


@app.route('/adminPortal/<user>')
def adminPortal(user):
    uri1 = "http://ec2-52-15-178-137.us-east-2.compute.amazonaws.com/visualization/apps_run_time_1month_all"
    uri2 = "http://ec2-52-15-178-137.us-east-2.compute.amazonaws.com/visualization/max_used_all"
    uri3 = "http://ec2-52-15-178-137.us-east-2.compute.amazonaws.com/visualization/min_used_all"

    # Last 7 days
    try:
        uResponse = requests.get(uri1)
    except requests.ConnectionError:
        return "Connection Error"
    Jresponse = uResponse.text
    data1 = json.loads(Jresponse)
    dataList1 = data1['result']

    for i in dataList1:
        index=i['app_name'].rfind('.')
        i['app_name']=i['app_name'][index + 1:].title()

    # Most used app global
    try:
        uResponse = requests.get(uri2)
    except requests.ConnectionError:
        return "Connection Error"
    Jresponse = uResponse.text
    data2 = json.loads(Jresponse)
    dataList2 = data2['result']
    index2 = dataList2['label'].rfind('.')
    dataList2['label'] = dataList2['label'][index2 + 1:].title()

    # Least used app global
    try:
        uResponse = requests.get(uri3)
    except requests.ConnectionError:
        return "Connection Error"
    Jresponse = uResponse.text
    data3 = json.loads(Jresponse)
    dataList3 = data3['result']
    index3 = dataList3['label'].rfind('.')
    dataList3['label'] = dataList3['label'][index3 + 1:].title()

    # dataList3['label']='Customer'
    # dataList3['value'] = '1'

    return render_template('adminPortal.html',tableData=dataList1,maxUsed=dataList2,leastUsed=dataList3,user=user)


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
   app.run(debug = True,host='0.0.0.0')