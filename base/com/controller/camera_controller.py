from base import app
from flask import Flask, request, redirect, render_template, jsonify
from base.com.vo.camera_vo import CameraVO
from base.com.dao.camera_dao import CameraDAO
from base.com.vo.branch_vo import BranchVO
from base.com.dao.branch_dao import BranchDAO

@app.route('/loadcamera')
def loadcamera():
    branch_dao=BranchDAO()
    branch_name=branch_dao.view_branch()
    return render_template("admin/addCamera.html",branch_name=branch_name)

@app.route('/addcamera',methods=['POST'])
def addcamera():
    camera_vo=CameraVO()
    camera_dao=CameraDAO()

    camera_name=request.form.get('camera_name')
    camera_model=request.form.get('camera_model')
    camera_location=request.form.get('camera_location')
    camera_branch_id=request.form.get('camera_branch')
    camera_field_of_vision=request.form.get('camera_field_of_vision')
    camera_resolution=request.form.get('camera_resolution')
    camera_recording_mode=request.form.get('camera_recording_mode')

    camera_vo.camera_name=camera_name
    camera_vo.camera_model=camera_model
    camera_vo.camera_location=camera_location
    camera_vo.camera_branch_id=camera_branch_id
    camera_vo.camera_field_of_vision=camera_field_of_vision
    camera_vo.camera_resolution=camera_resolution
    camera_vo.camera_recording_mode=camera_recording_mode

    camera_dao.insert_camera(camera_vo)

    return redirect("/addDetection")

@app.route("/viewcamera")
def viewcamera():
    camera_dao=CameraDAO()
    camera_vo_list=camera_dao.view_camera()
    return render_template("admin/viewCamera.html", camera_vo_list=camera_vo_list)

@app.route("/deletecamera",methods=['POST','GET'])
def deletecamera():
    camera_vo=CameraVO()
    camera_dao=CameraDAO()

    camera_id=request.args.get("camera_id")

    camera_vo.camera_id=camera_id
    camera_dao.delete_camera(camera_vo)

    return redirect("/viewcamera")

@app.route('/editcamera',methods=['POST','GET'])
def editcamera():
    camera_vo=CameraVO()
    camera_dao=CameraDAO()

    camera_id=request.args.get("camera_id")
    camera_vo.camera_id=camera_id
    camera_vo_list=camera_dao.edit_camera(camera_vo)
    branch_dao = BranchDAO()
    branch_name = branch_dao.view_branch()

    return render_template("admin/editCamera.html",camera_vo_list=camera_vo_list,branch_name=branch_name)

@app.route('/updatecamera',methods=['POST','GET'])
def updatecamera():
    camera_vo = CameraVO()
    camera_dao = CameraDAO()
    camera_id=request.form.get('camera_id')
    camera_name = request.form.get('camera_name')
    camera_model = request.form.get('camera_model')
    camera_location = request.form.get('camera_location')
    camera_branch_id = request.form.get('camera_branch')
    camera_field_of_vision = request.form.get('camera_field_of_vision')
    camera_resolution = request.form.get('camera_resolution')
    camera_recording_mode = request.form.get('camera_recording_mode')
    camera_vo.camera_id=camera_id
    camera_vo.camera_name = camera_name
    camera_vo.camera_model = camera_model
    camera_vo.camera_location = camera_location
    camera_vo.camera_branch_id = camera_branch_id
    camera_vo.camera_field_of_vision = camera_field_of_vision
    camera_vo.camera_resolution = camera_resolution
    camera_vo.camera_recording_mode = camera_recording_mode

    camera_dao.update_camera(camera_vo)
    return redirect("/viewcamera")

@app.route('/ajaxcamera',methods=['POST','GET'])
def ajaxcamera():
    camera_dao=CameraDAO()
    camera_vo=CameraVO()
    camera_branch_id=request.args.get('detection_branch_id')
    camera_vo.camera_branch_id=camera_branch_id
    camera_name=camera_dao.get_camera(camera_vo)
    camera_ajax_list = [i.as_dict() for i in camera_name]
    return jsonify(camera_ajax_list)


