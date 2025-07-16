from base import app
from flask import Flask,render_template,redirect,request
from base.com.dao.county_dao import CountryDAO
from base.com.vo.state_vo import StateVO
from base.com.dao.state_dao import StateDAO

@app.route("/loadState")
def loadState():
    country_dao=CountryDAO()
    country_name=country_dao.view_country()
    return render_template("admin/state.html",country_name=country_name)

@app.route("/addState",methods=['POST'])
def addState():
    state_country_id=request.form.get("select_country")
    state_name=request.form.get("select_state")
    state_vo=StateVO()
    state_dao=StateDAO()
    state_vo.state_name=state_name
    state_vo.state_country_id=state_country_id
    state_dao.insert_state(state_vo)
    return redirect("/")

@app.route("/viewState")
def viewState():
    state_dao=StateDAO()
    state_vo_list=state_dao.view_state()
    return render_template("admin/viewState.html",state_vo_list=state_vo_list)

