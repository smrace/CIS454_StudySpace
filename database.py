from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#@app.route("/")

app.config['SQLALCHEMY_DATABASE_URI'] = '_sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(20), nullable=False)
    lastName = db.Column(db.String(20), nullable=False)
    emailAddress = db.Column(db.String(75), unique=True, nullable=False)
    userProfile = db.Column(db.String(20), nullable=False, default='default.jpg')
    userType = db.Column(db.String(10),nullable=False, default='Student')
    loginName = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(40),nullable=False)

    def __repr__(self):
        return f"User('{self.firstName}', '{self.lastName}', '{self.emailAddress}', '{self.userProfile}', '{self.userType}', '{self.loginName}', '{self.password}') "

class Building(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    floor = db.Column(db.Integer, nullable=False)
    lattitude = db.Column(db.String(50), nullable=False)
    longitude = db.Column(db.String(50), nullable=False)
    openHour = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    closeHour = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)    

    def __repr__(self):
        return f"Building('{self.name}', '{self.floor}', '{self.lattitude}', '{self.longitude}', '{self.openHour}', '{self.closeHour}') "


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    size = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f"Group('{self.size}') "


class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    building_id = db.Column(db.Integer, db.ForeignKey('building.id'), nullable=False)
    amenities_id = db.Column(db.Integer, db.ForeignKey('amenities.id'), nullable=False)
    roomNumber = db.Column(db.Integer, nullable=False)
    roomType = db.Column(db.String(20), nullable=False)
    roomCapactiy = db.Column(db.Integer, nullable=False)


    def __repr__(self):
        return f"Room('{self.roomNumber}', '{self.roomType}', '{self.roomCapactiy}')"

class Amenities(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amenityName = db.Column(db.String(30), nullable=False)
    amenityType = db.Column(db.String(40), nullable=False)

    def __repr__(self):
        return f"Amenities('{self.amenityName}', '{self.amenityType}')"

class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subjectName = db.Column(db.String(40), unique=True, nullable=True)
    
    def __repr__(self):
        return f"Subject('{self.subjectName}')"


class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)
    building_id = db.Column(db.Integer, db.ForeignKey('building.id'), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    datetimeReserved = db.Column(db.DateTime, nullable=False)
    totalHours = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Reservation('{self.datetimeReserved}', '{self.totalHours}')"

class RoomAmenities(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    raRoom_id = db.Column(db.Integer, nullable=False)
    raAmenity_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Reservation('{self.raRoom_id}', '{self.raAmenity_id}')"

class StudentSubject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    raRoom_id = db.Column(db.Integer, nullable=False)
    raAmenity_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Reservation('{self.raRoom_id}', '{self.raAmenity_id}')"



if __name__ == '__main__':
    app.run(debug = True)