from base import app
from flask import Flask,render_template,redirect,request
from base.com.vo.country_vo import CountryVO
from base.com.dao.county_dao import CountryDAO
from base.com.vo.state_vo import StateVO
from base.com.dao.state_dao import StateDAO
from base.com.vo.city_vo import CityVO
from base.com.dao.city_dao import CityDAO
from base.com.vo.branch_vo import BranchVO
from base.com.dao.branch_dao import BranchDAO

@app.route('/addbranch')
def addbranch():
    country_dao=CountryDAO()
    country_vo=CountryVO()
    country_name=country_dao.view_country()
    return render_template("admin/addBranch.html",country_name=country_name)

@app.route('/insertbranch',methods=['POST'])
def insertbranch():
    branch_name=request.form.get('branch_name')
    branch_country=request.form.get('branch_country_id')
    branch_state=request.form.get('branch_state_id')
    branch_city=request.form.get("branch_city_id")
    branch_contact=request.form.get("branch_contact")
    branch_manager=request.form.get("branch_manager")
    branch_timings=request.form.get("branch_timings")
    branch_days=request.form.get("branch_operation")

    branch_vo=BranchVO()
    branch_dao=BranchDAO()

    branch_vo.branch_name=branch_name
    branch_vo.branch_country=branch_country
    branch_vo.branch_state=branch_state
    branch_vo.branch_city=branch_city
    branch_vo.branch_contact=branch_contact
    branch_vo.branch_manager=branch_manager
    branch_vo.branch_timings=branch_timings
    branch_vo.branch_days=branch_days

    branch_dao.insert_branch(branch_vo)

    return redirect("/loadcamera")

@app.route('/viewbranch')
def viewbranch():
    branch_dao=BranchDAO()
    branch_vo_list=branch_dao.view_branch()
    return render_template("admin/viewBranch.html", branch_vo_list=branch_vo_list)

@app.route('/deletebranch',methods=['POST','GET'])
def deletebranch():
    branch_id=request.args.get('branch_id')
    branch_vo=BranchVO()
    branch_dao=BranchDAO()

    branch_vo.branch_id=branch_id
    branch_dao.delete_branch(branch_vo)

    return redirect("/viewbranch")


@app.route("/editbranch",methods=['POST','GET'])
def editbranch():
    country_vo=CountryVO()
    country_dao=CountryDAO()

    country_name = country_dao.view_country()
    branch_id=request.args.get("branch_id")
    branch_vo=BranchVO()
    branch_dao=BranchDAO()
    branch_vo.branch_id=branch_id

    branch_vo_list=branch_dao.edit_branch(branch_vo)

    return render_template("admin/editBranch.html",branch_vo_list=branch_vo_list,country_name=country_name)

@app.route("/updatebranch",methods=['POST'])
def updatebranch():
    branch_id=request.form.get("branch_id")
    branch_name = request.form.get('branch_name')
    branch_country = request.form.get("branch_country_id")
    branch_state = request.form.get("branch_state_id")
    branch_city = request.form.get("branch_city_id")
    branch_contact = request.form.get("branch_contact")
    branch_manager = request.form.get("branch_manager")
    branch_timings = request.form.get("branch_timings")
    branch_days = request.form.get("branch_operation")

    branch_vo = BranchVO()
    branch_dao = BranchDAO()

    branch_vo.branch_id=branch_id
    branch_vo.branch_name = branch_name
    branch_vo.branch_country = branch_country
    branch_vo.branch_state = branch_state
    branch_vo.branch_city = branch_city
    branch_vo.branch_contact = branch_contact
    branch_vo.branch_manager = branch_manager
    branch_vo.branch_timings = branch_timings
    branch_vo.branch_days = branch_days
    branch_dao.update_branch(branch_vo)
    return redirect("/viewbranch")
