from base import app
from flask import Flask,render_template,redirect,request
from base.com.vo.country_vo import CountryVO
from base.com.dao.county_dao import CountryDAO

@app.route("/loadCountry")
def loadCountry():
    return render_template("admin/country.html")

@app.route("/addCountry",methods=['POST'])
def addCountry():
    country_name=request.form.get("select_country")
    print(">>>>>>>>>>>",country_name)
    country_vo=CountryVO()
    country_dao=CountryDAO()
    country_vo.country_name=country_name
    country_dao.insert_country(country_vo)
    return redirect("/")

@app.route("/viewCountry")
def viewCountry():
    country_dao=CountryDAO()
    country_vo_list=country_dao.view_country()
    return render_template("admin/viewCountry.html",country_vo_list=country_vo_list)

