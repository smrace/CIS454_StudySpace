from datetime import datetime
from studyspace import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#UserMixin is used to help login a user


#UserClass hold all User information in the database
class User(db.Model, UserMixin):
    #user_id is the primary key (unique identifier) that distinguishes one user from another
        #Each primary key must be an integer type
    id = db.Column(db.Integer, primary_key=True)
    #first is the first name of a user
        #When the element is set to nullable FALSE, each database entry requires an input for the first name
            #If a first name is not included in the database upon entry, it will default to "Student First Name" instead
    first = db.Column(db.String(20), nullable=False, default='Student First Name')
    #last is the first name of a user
        #The datatype for the first and last name are strings that allow up to 20 characters 
    last = db.Column(db.String(20), nullable=False, default='Student Last Name')
    #emailAddress asks for the user's email address upon registering to the site
        #When unique is set to TRUE, no two entries in the User database can contain the same email address
    emailAddress = db.Column(db.String(75), unique=True, nullable=False)
    #password for a user's account
    password = db.Column(db.String(40), nullable=False)
<<<<<<< Updated upstream
    major = db.Column(db.String(40), nullable=False)
    study = db.Column(db.String(40), nullable=False)
=======
    #major takes in the User's primary major or field of study in which the university accepted them for
    major = db.Column(db.String(40), nullable=False, default='Computer Science')
    #study looks for the specific course that a User is interested in matching with someone else for to study
    study = db.Column(db.String(40), nullable=False, default='MAT 101')
    #groups is a relationship call that allows for attributes of the User class to be called in the group class
>>>>>>> Stashed changes
    groups = db.relationship('Group', backref='groupName', lazy=True)
    #backref takes an attribute from the class in which the User class is associated with to cross verify inputted information
        #when lazy is set to True, the objects from queries are loaded without other related objects returning
    reservation = db.relationship('Reservation', backref='reservationUser', lazy=True) 

    #This return statement will give all the attributes that are returned when the database is updated with more information
    def __repr__(self):
        return f"User('{self.first}', '{self.last}', '{self.emailAddress}', '{self.password}', '{self.major}', '{self.study}') "

#BuildingClass contains all the information of the buildings that are located on campus
class Building(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    openHour = db.Column(db.String(10), nullable=False)
    closeHour = db.Column(db.String(10), nullable=False)
    rooms = db.relationship('Room', backref='roomNumber', lazy=True) 
    reservation = db.relationship('Reservation', backref='reservationLocation', lazy=True) 

    def __repr__(self):
        return f"Building('{self.name}', '{self.openHour}', '{self.closeHour}') "


#GroupClass houses all the information when users select to others to create a group with
class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #user_id is a foreign key which allows for the group class to refer to attributes of the User class to access that information
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
<<<<<<< Updated upstream
    studyType = db.Column(db.Boolean, nullable=True)
=======
    #studyType asks for whether a students wants to study by themselves or in a group and returns in in a string
    studyType = db.Column(db.String(10), nullable=False)
>>>>>>> Stashed changes
    size = db.Column(db.Integer, nullable=False)
    reservation = db.relationship('Reservation', backref='reservationGroup', lazy=True) 
    
    def __repr__(self):
        return f"Group('{self.user_id}','{self.studyType}', '{self.size}') "

#RoomClass holds information on all the room that are available to book at the University
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

#AmenitiesClass contains all the extra gadgets that students would be interested in having in their rooms they reserve
class Amenities(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    amenityType = db.Column(db.String(40), nullable=False)
    room = db.relationship('Room', backref='roomAmenities', lazy=True) 

    def __repr__(self):
        return f"Amenities('{self.name}', '{self.amenityType}')"

#SubjectClass holds multiple available subjects that a student may potentially be interested in reserving
class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True, nullable=True)
    
    def __repr__(self):
        return f"Subject('{self.name}')"

#ReservationClass is a database that aggreates accessible information from the other classes when a user looks to book a room on campus
class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)
    building_id = db.Column(db.Integer, db.ForeignKey('building.id'), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    #When a user registers for a room to be reserved, the time in which they reserved will be marked down using a DateTime datatype, matching current timings
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

