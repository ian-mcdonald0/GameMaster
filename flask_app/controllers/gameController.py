from flask_app import app
from flask import render_template, redirect, request, flash, session


#### START ####
@app.route('/')
def display():
    return render_template('Dashboard.html')

@app.route('/game/new')
def gameNew():
    return render_template('GameCreate.html')