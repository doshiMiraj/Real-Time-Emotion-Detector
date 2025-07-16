from base import app
from flask import Flask,render_template,redirect,request
from base.com.vo.detection_vo import DetectionVO
from base.com.service import ai_code
from base.com.vo.detection_vo import DetectionVO
from base.com.dao.detection_dao import DetectionDAO
from base.com.vo.branch_vo import BranchVO
from base.com.dao.branch_dao import BranchDAO
from base.com.dao.camera_dao import CameraDAO
from base.com.vo.camera_vo import CameraVO
from base.com import service
import datetime
import time

@app.route('/addDetection',methods=["POST",'GET'])
def adddetction():
    branch_dao=BranchDAO()
    branch_vo=BranchVO()

    branch_name = branch_dao.view_branch()
    return render_template("admin/addDetection.html",branch_name=branch_name)

@app.route('/insertDetection',methods=['POST'])
def insertdetection():
    before = datetime.datetime.now()

    detection_list = ai_code.show_webcam()
    after = datetime.datetime.now()
    neutral = detection_list['neutral']
    sad = detection_list['sad']
    happy = detection_list['happy']
    angry = detection_list['angry']
    fear = detection_list['fear']
    disgust = detection_list['disgust']
    surprise = detection_list['surprise']
    list=[neutral,happy,sad,angry,disgust,surprise,fear]
    detection_branch_id=request.form.get('detection_branch_id')
    detection_camera_id=request.form.get('detection_camera_id')
    print(list)
    epoch_time = int(time.time())
    print(epoch_time)
    time_stamp=datetime.datetime.utcfromtimestamp(epoch_time)
    print(time_stamp)
    time_stamp=str(time_stamp)
    print(time_stamp)
    time_stamp=time_stamp.split()
    print(time_stamp)
    date=time_stamp[0]
    detection_time=time_stamp[1]
    detection_dao = DetectionDAO()
    detection_vo = DetectionVO()
    detection_vo.detection_time=detection_time
    detection_vo.detection_date=date
    detection_vo.sad_count=sad
    detection_vo.surprise_count=surprise
    detection_vo.neutral_count=neutral
    detection_vo.happy_count=happy
    detection_vo.fear_count=fear
    detection_vo.disgust_count=disgust
    detection_vo.angry_count=angry
    detection_vo.detection_camera_id=detection_camera_id
    detection_vo.detection_branch_id=detection_branch_id
    detection_dao.insert_detection(detection_vo)
    return redirect("/viewDetection")

@app.route("/viewDetection",methods=['POST','GET'])
def viewDetection():
    detection_vo=DetectionVO()
    detection_dao=DetectionDAO()
    detection_vo_list=detection_dao.view_detection()
    return render_template("admin/viewDetection.html",detection_vo_list=detection_vo_list)

@app.route("/deleteDetection",methods=['POST','GET'])
def deletedetection():
    detection_vo=DetectionVO()
    detection_dao=DetectionDAO()

    detection_id=request.args.get('detection_id')

    detection_vo.detection_id=detection_id
    detection_dao.delete_detection(detection_vo)
    return redirect("/viewDetection")

