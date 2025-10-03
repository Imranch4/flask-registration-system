from flask import render_template, request, redirect, session, url_for
from models.user import User, db

def init_auth_routes(app):
    @app.route('/')
    def home():
        if "username" in session:
            return redirect(url_for('dashboard'))
        return render_template('login.html')

    @app.route('/login', methods=['GET', 'POST']) 
    def login():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']

            user = User.query.filter_by(username=username).first()
            
            if user and user.check_password(password):
                session['username'] = user.username
                return redirect('/dashboard')
            else:
                return render_template('login.html', error='Invalid user')

        return render_template('login.html')

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            nom = request.form['nom']
            prenom = request.form['prenom']
            username = request.form['username']
            genre = request.form.get('genre')
            email = request.form['email']
            password = request.form['password']

            existing_user = User.query.filter((User.email == email) | (User.username == username)).first()
            if existing_user:
                return render_template('register.html', error="Email or Username already exists!")

            new_user = User(nom=nom, prenom=prenom, username=username, email=email, genre=genre, password=password)
            db.session.add(new_user)
            db.session.commit()
            return redirect('/login')

        return render_template('register.html')

    @app.route('/dashboard')
    def dashboard():
        if 'username' in session:
            user = User.query.filter_by(username=session['username']).first()
            if user:  
                return render_template('dashboard.html', user=user)
        return redirect('/login') 

    @app.route('/logout')
    def logout():
        session.pop('username', None)
        return redirect(url_for('login'))