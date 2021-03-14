from flask import Flask, render_template, url_for
app = Flask(__name__)
from flask_bcrypt import Bcrypt


bcrypt = Bcrypt(app)

@app.route("/")
@app.route("/home")
def home():
    return render_template('login.html')

@app.route("/login")
def login():
    return render_template('login.html', title='Login')

@app.route("/createAccount")
def createAccount():
    return render_template('createAccount.html', title='Create Account')

@app.route("/mainPage")
def mainPage():
    return render_template('mainPage.html', title='Main Page')

@app.route("/about")
def about():
    return render_template('about.html', title='about')

@app.route("/findGroup")
def findGroup():
    return render_template('findGroup.html', account=accounts, title='Find Group')

#findGroup.html needs to be looked at because it does not print out what anything
#line 52 in layout.html has further details on buttons needing work
#Look into changing the color of the whole webpage
    #This will be in main.css


 #student profile class. ideally this would save itself between user uses but idk how to do that
class StudentProfile:
    lst = []
    
   
    def __init__(self,subject,partner,name,email):
        self.s = subject
        self.p = partner
        self.n = name
        self.e = email
        
    
        if(partner == True):
            self.lst.append(self.n)
            self.lst.append(self.s)
    def chgsbj(self, sub):
        subject=sub
        self.s =subject

#call this when creating password for first time
def crypter(password):
    pw_hash = bcrypt.generate_password_hash(passkey).decode("utf-8")
    #line to upload pw hash to data base
    #user.password = pw_hash
    #db.session.add(user)
    #db.session.commit()

#call this when authenticating
def authenticator(attempted_pass):
    if bcrypt.check_password_hash(database.get.pwh, attempted_pass):
       return redirect(url_for('mainPage'))
    else :
        #flash(f'Wrong password to the entered username. Please try again.')
        return redirect(url_for('login'))
    
    


accounts = [ StudentProfile("science",True,'John Doe', 'johndoe@syr.edu'),
                    StudentProfile("math",True,'Jane Doe', 'janedoe@syr.edu'),
                    StudentProfile("statistics",True,'Grumpy Gus', 'ggus@syr.edu')
                    ]

if __name__ == '__main__':
    app.run(debug = True)

