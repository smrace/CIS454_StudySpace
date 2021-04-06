# CIS454_StudySpace
# Files included/necessary that are not in the studyspace folder  
routes.py, site.db, forms.py, app.py, __init__.py, site.db


# Files in the studyspace folder are all needed  
about.html, birdLibrary.html, confirmation.html, createAccount.html, falk.html, findGroup.html,
layout.html, lifeScienceBuilding.html, link.html, login.html, mainPage.html, map.html, 
newhouse.html, newSurvey.html, profile.html, survey.html, whitman.html, main.css


# How to set up environment  
Please ensure that your python version is Python3.7.0  
Install Visual Studio code  
-Run the command python3 -m venv venv  
-Then run command source venv/bin/activate  
This may have to be subsituted for .venv/bin/activate  
If on Windows, the commands may not work. If they do not work  
FOR WINDOWS  
-Run command py -3 -m venv venv  
-Then run command venv\Scripts\activate


# pip installs needed  
pip install flask, pip install flask-sqlalchemy, pip install flask-wtf, pip install email_validator,
pip install flask-bcrypt, pip install flask-login


# How to run  
Once everything is installed and the environment is set up with all of the files needed, run the website by running app.py as a flask application through the drop-down menu.

# Known bugs    
-Entering a room number to confirm a room reservation fills out all confirm room fields for each room in all building pages.  
-User stays logged in even if remember me is not selected  when logging in.  

# Unfinished Features
-In the survey when a radio button is not selected and the user attempts to submit, there is no error message prompted. If we had more time, this would have been implemented. Due to group discussions, this was deemed less important to complete than other finalized features.  
-When reserving a room, the inputted room number is not checked to make sure it matches the room number of the room being reserved.  
-When reserving a room, the inputted room number is not checked to make sure it matches a room number in the database.  
-When reserving a room, the inputted room number is not check to make sure that the room has not already been reserved. Rooms can be double booked.  
-When cancelling a reservation, the reservation is not actually cancelled.  
-The Forgot Password? button does not work when attempting to log in.  
-If given more time, have external user with administrative credentials update buildings and rooms in the database. 


