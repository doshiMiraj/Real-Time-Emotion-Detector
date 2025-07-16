from base import app
from flask import Flask, render_template, redirect, request, jsonify
from base.com.vo.country_vo import CountryVO
from base.com.dao.county_dao import CountryDAO
from base.com.dao.state_dao import StateDAO
from base.com.vo.state_vo import StateVO
from base.com.dao.city_dao import CityDAO
from base.com.vo.city_vo import CityVO

@app.route("/loadCity")
def loadCity():
    country_dao=CountryDAO()
    country_name=country_dao.view_country()
    return render_template("admin/city.html",country_name=country_name)

@app.route("/addState",methods=['POST','GET'])
def addstate():
    city_country_id=request.args.get("city_country_id")
    state_vo=StateVO()
    state_dao=StateDAO()
    state_vo.state_country_id=city_country_id
    state_vo_list=state_dao.get_state(state_vo)
    print(">>>>>>>>>",state_vo_list)

    state_ajax_list=[i.as_dict() for i in state_vo_list]
    print(">>>>>>>>>",state_ajax_list)
    return jsonify(state_ajax_list)

@app.route("/addCity",methods=["POST","GET"])
def addCity():
    city_name=request.form.get("city_name")
    city_country_id=request.form.get("city_country_id")
    city_state_id=request.form.get("city_state_id")

    city_vo=CityVO()
    city_dao=CityDAO()
    print(">>>>>>>>",city_country_id)
    city_vo.city_name=city_name
    city_vo.city_state_id=city_state_id
    city_vo.city_country_id=city_country_id

    city_dao.insert_city(city_vo)
    return redirect("/")

@app.route("/viewCity")
def viewCity():
    city_dao=CityDAO()
    city_vo_list=city_dao.view_city()
    return render_template("admin/viewCity.html",city_vo_list=city_vo_list)

@app.route("/ajaxcity")
def ajaxcity():
    city_vo=CityVO()
    city_dao=CityDAO()
    city_state_id=request.args.get("branch_state_id")
    print(">>>>>>>",city_state_id)
    city_vo.city_state_id=city_state_id
    city_name=city_dao.get_city(city_vo)
    city_ajax_list=[i.as_dict() for i in city_name]
    return jsonify(city_ajax_list)
