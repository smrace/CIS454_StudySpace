from datetime import datetime
from studyspace import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#UserMixin is used to help login a user
#the first and last name were giving me issues so they may have to be modified. Might not be up to date with site.db
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first = db.Column(db.String(20), nullable=False, default='Student First Name')
    last = db.Column(db.String(20), nullable=False, default='Student Last Name')
    emailAddress = db.Column(db.String(75), unique=True, nullable=False)
    password = db.Column(db.String(40), nullable=False)
    major = db.Column(db.String(40), nullable=False, default='Computer Science')
    study = db.Column(db.String(40), nullable=False, default='MAT 101')
    groups = db.relationship('Group', backref='groupName', lazy=True)
    reservation = db.relationship('Reservation', backref='reservationUser', lazy=True) 

    def __repr__(self):
        return f"User('{self.first}', '{self.last}', '{self.emailAddress}', '{self.password}', '{self.major}', '{self.study}') "

class Building(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    openHour = db.Column(db.String(10), nullable=False)
    closeHour = db.Column(db.String(10), nullable=False)
    rooms = db.relationship('Room', backref='roomNumber', lazy=True) 
    reservation = db.relationship('Reservation', backref='reservationLocation', lazy=True) 

    def __repr__(self):
        return f"Building('{self.name}', '{self.openHour}', '{self.closeHour}') "


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    studyType = db.Column(db.String(10), nullable=False)
    size = db.Column(db.Integer, nullable=False)
    reservation = db.relationship('Reservation', backref='reservationGroup', lazy=True) 
    
    def __repr__(self):
        return f"Group('{self.user_id}','{self.studyType}', '{self.size}') "


class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    building_id = db.Column(db.Integer, db.ForeignKey('building.id'), nullable=False)
    amenities_id = db.Column(db.Integer, db.ForeignKey('amenities.id'), nullable=False)
    name = db.Column(db.String(10), unique=True, nullable=False)
    floor = db.Column(db.String(10), nullable=False)
    roomType = db.Column(db.String(20), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    reservation = db.relationship('Reservation', backref='reservationRoom', lazy=True) 


    def __repr__(self):
        return f"Room('{self.building_id}', '{self.amenities_id}', '{self.name}', '{self.floor}', '{self.roomType}', '{self.capacity}')"

class Amenities(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    amenityType = db.Column(db.String(40), nullable=False)
    room = db.relationship('Room', backref='roomAmenities', lazy=True) 

    def __repr__(self):
        return f"Amenities('{self.name}', '{self.amenityType}')"

class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True, nullable=True)
    
    def __repr__(self):
        return f"Subject('{self.name}')"


class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)
    building_id = db.Column(db.Integer, db.ForeignKey('building.id'), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    datetimeReserved = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    totalHours = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Reservation('{self.room_id}','{self.building_id}','{self.group_id}','{self.user_id}','{self.datetimeReserved}', '{self.totalHours}')"

class RoomAmenities(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    raRoom_id = db.Column(db.Integer, nullable=False)
    raAmenity_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"RoomAmenities('{self.raRoom_id}', '{self.raAmenity_id}')"

class StudentSubject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ssStudent_id = db.Column(db.Integer, nullable=False)
    ssSubject_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"StudentSubject('{self.ssStudent_id}', '{self.sssubject_id}')"

