from flask import Flask, render_template, url_for
app = Flask(__name__)

accounts = [
    {
        'name': 'John Doe',
        'lookingforgroup': 'Yes',
        'subject': 'Science',
        'email': 'johndoe@syr.edu'
    },
    {
        'name': 'Jane Doe',
        'lookingforgroup': 'Yes',
        'subject': 'Math',
        'email': 'janedoe@syr.edu'
    },
    {
        'name': 'Grumpy Gus',
        'lookingforgroup': 'Yes',
        'subject': 'Statistics',
        'email': 'ggus@syr.edu'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('mainPage.html')

@app.route("/login")
def login():
    return render_template('login.html', title='Login')

@app.route("/createAccount")
def createAccount():
    return render_template('createAccount.html', title='Create Account')

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


if __name__ == '__main__':
    app.run(debug = True)

