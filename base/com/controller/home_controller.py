from base import app
from flask import Flask,render_template,redirect,request

@app.route('/')
def home():
    return render_template("admin/index.html")


