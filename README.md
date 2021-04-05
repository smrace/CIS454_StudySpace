# CIS454_StudySpace
# Files included/necessary not in the studyspace folder  
routes.py, site.db, forms.py, app.py, __init__.py


# Files in the studyspace folder are all need  
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
Run the website by running app.py as a flask application through the drop-down menu

# Known bugs    
Currently the reservations that are cancelled are not updated in the database 

# Unfinished Features
In the survey when a radio button is not selected and the user attempts to submit, there is no error message prompted. If we had more time, this would have been implemented. Due to group discussions, this was deemed less important to complete than other finalized features.


