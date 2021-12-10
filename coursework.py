from flask import Flask, url_for, render_template
app = Flask(__name__)

@app.route('/')
def home():
	return render_template("home.html")
  
@app.route('/signup')
def signup():
    return render_template("signup.html")  
  
@app.route('/login')
def login():
    return render_template("login.html")
    
@app.route('/account')
def account():
	return render_template("account.html")
    
@app.route('/dashboard')
def dashboard():
	return render_template("dashboard.html")
    
@app.route('/settings')
def settings():
	return render_template("settings.html")
    
if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)