from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, Response, redirect, url_for, request, session, abort




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://mahmoud:123@localhost:5432/robot'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["IMAGE_UPLOADS"] = 'uploads'


db = SQLAlchemy(app)



def getcurrent_date():
    from datetime import datetime
    # datetime object containing current date and time
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return str(dt_string)






class Robot(db.Model):
  __tablename__ = 'robot'
  id = db.Column(db.Integer, primary_key=True)
  robot_name = db.Column(db.String(), default='Oracle Chat Bot')
  robot_image = db.Column(db.String(), default='mr_robot.jpg')
  key_name = db.Column(db.String(), default='')
  key_value = db.Column(db.String(),default='')
  key_time = db.Column(db.String(), nullable=False, default=getcurrent_date())
  exp = db.Column(db.Float, nullable=False, default=0)
  #children = relationship("Child", order_by="Child.id")
  #todo = db.relationship('todo', backref="some_paret", lazy=True)
  #children = db.relationship('Todo', backref='some_parent', lazy=True)


  def __repr__(self):
    return "<Robot ID: {}, name: {}>".format(self.key_time, self.key_value)



class APIStore(db.Model):
  __tablename__ = 'api_store'
  id = db.Column(db.Integer, primary_key=True)
  robot_id = db.Column(db.Integer, db.ForeignKey('robot.id'))
  robot = db.relationship(Robot)

  def __repr__(self):
    return "<sore ID: {}, name: {}>".format(self.id, self.robot_id)

class API(db.Model):
  __tablename__ = 'api'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(), nullable=False)
  baseurl = db.Column(db.String(), nullable=False)
  baseurl1 = db.Column(db.String(), nullable=False)
  api_key = db.Column(db.String(), nullable=False)
  #id
  query0 = db.Column(db.String(), nullable=True, default=None)
  #zip
  query1 = db.Column(db.String(), nullable=True, default=None)
  #units
  query2 = db.Column(db.String(), nullable=True, default=None)
  #q= city name
  query3 = db.Column(db.String(), nullable=True, default=None)
  #q=state code
  query4 = db.Column(db.String(), nullable=True, default=None)
  #q=country code
  query5 = db.Column(db.String(), nullable=True, default=None)
  #mode
  query6 = db.Column(db.String(), nullable=True, default=None)
  #lang
  query7 = db.Column(db.String(), nullable=True, default=None)
  #lat
  query8 = db.Column(db.String(), nullable=True, default=None)
  #lon
  query9 = db.Column(db.String(), nullable=True, default=None)
  # price
  api_price = db.Column(db.Float, nullable=False,default=0)
  # desc
  api_description = db.Column(db.String(), nullable=False)
  # document
  apid_document = db.Column(db.String(), nullable=False)
  # logo
  api_image = db.Column(db.String(), nullable=False)
  # add abbilites
  query_id = db.Column(db.Boolean(), nullable=True, default=False)
  query_zip = db.Column(db.Boolean(), nullable=True, default=False)
  query_countrycode = db.Column(db.Boolean(), nullable=True, default=False)
  query_location = db.Column(db.Boolean(), nullable=True, default=False)

  store_id = db.Column(db.Integer, db.ForeignKey('api_store.id'))
  store = db.relationship(APIStore)
  robot_id = db.Column(db.Integer, db.ForeignKey('robot.id'))
  robot = db.relationship(Robot)

  #children = relationship("Child", order_by="Child.id")
  #todo = db.relationship('todo', backref="some_paret", lazy=True)
  #children = db.relationship('Todo', backref='some_parent', lazy=True)

  def __repr__(self):
    return "<Api Baseurl: {}, name: {}>".format(self.baseurl, self.name)



db.create_all()
