from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Fcuser( db.Model ):
    __tablename__ = "fcuser"
    id = db.Column(db.Integer, primary_key=True )
    password = db.Column(db.String(64) )
    userid = db.Column( db.String(32) )
    username = db.Column( db.String(8) )

class LED_nomdle( db.Model ):
    __tablename__ = "led_seki"
    id = db.Column( db.Integer, primary_key=True )
    red = db.Column( db.Integer )
    green = db.Column( db.Integer )
    yellow = db.Column( db.Integer )
    status = db.Column( db.String(20) )
    time = db.Column( db.String(24) )