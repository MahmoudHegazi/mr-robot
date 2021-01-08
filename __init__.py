#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import render_template, jsonify, flash
from flask_sqlalchemy import SQLAlchemy

import requests
import os
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from database import API, APIStore, Robot, app, db
import sys


# return all users in the database
def query_robots_all():
    robot_list = Robot.query.all()
    db.session.close()
    return robot_list

# returl all posts in the database
def get_all_apis():
    api_list = API.query.all()
    db.session.close()
    return api_list


# returl all api by robot id
def query_api_all(robot_id):
    api_list = API.query.filter_by(robot_id=robot_id).all()
    db.session.close()
    return api_list

# return the Post  for the given post id
def getStoreByRobotId(robot_id):
    store = APIStore.query.filter_by(robot_id=robot_id).first()
    db.session.close()
    return store
# return the user  for the given user id
def getRobotById(robot_id):
    user = Robot.query.filter_by(id=robot_id).first()
    db.session.close()
    return user

# return all Posts created By the user_id given
def getBotApisById(robot_id):
    api_list = API.query.filter_by(robot_id=robot_id).all()
    db.session.close()
    return api_list

# return the robot by store id
def getRobotByStoreid(store_id):
    store_id = APIStore.query.filter_by(id=store_id).first()
    robot_id = store_id.robot_id
    robot = getRobotById(robot_id)
    db.session.close()
    return robot


# return the robot by api id
def getRobotByApiid(api_id):
    api = API.query.filter_by(id=api_id).first()
    robot_id = api.robot_id
    robot = getRobotById(robot_id)
    db.session.close()
    return robot


@app.route('/create_your_robot/<string:robot_name>/<string:image>', methods=['GET'])
def create_robot(robot_name, image):
    if request.method == 'GET':
        error = False
        #
        try:
            newRobot = Robot(robot_name=robot_name, robot_image=image)
            robot_name = newRobot.robot_name
            robot_image = newRobot.robot_image
            db.session.add(newRobot)
            store_for_robot = APIStore(robot_id=newRobot.id)
            db.session.add(store_for_robot)
            # it should be user api or get u and let him pay better and easier
            apikey = 'db6608063a9d72758e29ea323da07bd1'
            api = API(name='Current Weather Data', baseurl='api.openweathermap.org/data/2.5/weather?',
            baseurl1='api.openweathermap.org/data/2.5/find?',
            api_key=apikey, query0='id', query1='zip',
            query2='q', query3='units', query4='lang', query5='mode', query6='cnt', query7='lat',
            query8='lon', query9='cnt', api_price='1', api_description='Access current weather data\
            for any location including over 200,000 cities\
            We collect and process weather data from different\
            sources such as global and local weather models,\
            satellites, radars and vast network of weather stations\
            JSON, XML, and HTML formats Available for both Free and paid subscriptions',
            apid_document='https://openweathermap.org/current', api_image='logo_white_cropped.png', store_id=store_for_robot.id, robot_id=newRobot.id)

            db.session.commit()
        except:
            db.session.rollback()
            error = True
            # debug on make it return not print
            #print(sys.exc_info())
            return str(sys.exc_info())
            system_error_message = sys.exc_info()
        finally:
            db.session.close()
        if not error:
            print('Hello Robot')
            message = 'Great You Create Your New Robot WIth name: ' +  str(robot_name)
            message += '<br /> <br /><img width="200" height="200" src="/static/' + str(robot_image) + '">'
            message += '<br /> You Can Access Your API Sore And make your robot learn new APIs and do good things '
            return message
        else:
            return 'hi error'







@app.route('/admin_add_api/<string:admin_pass>')
def admin_add_api(admin_pass):
    if request.method == 'GET':
        error = False
        #
        try:
            newRobot = API(robot_name=robot_name, robot_image=image)
            robot_name = newRobot.robot_name
            robot_image = newRobot.robot_image
            db.session.add(newRobot)
            db.session.commit()
        except:
            db.session.rollback()
            error = True
            # debug on make it return not print
            #print(sys.exc_info())
            return str(sys.exc_info())
            system_error_message = sys.exc_info()
        finally:
            db.session.close()
        if not error:
            print('Hello Robot')
            message = 'Great You Create Your New Robot WIth name: ' +  str(robot_name)
            message += '<br /> <br /><img width="200" height="200" src="/static/' + str(robot_image) + '">'
            return message
        else:
            return 'hi error'





@app.route('/robot_profile/<int:robot_id>')
def profile(robot_id):
    robot = Robot.query.filter_by(id=robot_id).first()
    #todos = Todo.query.order_by('id').all()
    api_store = getStoreByRobotId(robot_id)
    api_list = query_api_all(robot_id)
    return render_template('robot.html',robot=robot)



if __name__ == '__main__':
    app.secret_key = 'S&Djry636qyye217773ddfJJK&(488_=-*1~!{L01}046%%^&45&&#^$^^y___'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
