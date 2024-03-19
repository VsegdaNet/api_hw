from flask import Flask, redirect, render_template, request, url_for, make_response
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_database.db'

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=True)
    email = db.Column(db.String(80), nullable=True)
    password = db.Column(db.String(80), nullable=True)

    def __reper__(self):
        return "<Article %r>" % self.id
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/finelogin')
def finelogin():
    return render_template('finelogin.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            return redirect('/')
        else:
            return "404"
    return render_template('/login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user = User(username=username, email=email)
        user.set_password(password)
        try:
            db.session.add(user)
            db.session.commit()
            return redirect('/finelogin')
        except:
            return "404"
    return render_template('/register')

if __name__ == "__main__":
    app.run(debug=True)