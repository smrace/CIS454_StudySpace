from flask import Flask, render_template, url_for
app = Flask(__name__)




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
    

accounts = [ StudentProfile("science",True,'John Doe', 'johndoe@syr.edu'),
                    StudentProfile("math",True,'Jane Doe', 'janedoe@syr.edu'),
                    StudentProfile("statistics",True,'Grumpy Gus', 'ggus@syr.edu')
                    ]

if __name__ == '__main__':
    app.run(debug = True)

