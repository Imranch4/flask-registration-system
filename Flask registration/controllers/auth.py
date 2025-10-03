from flask import render_template, request, redirect, session, url_for, flash
import os
from werkzeug.utils import secure_filename
from models.user import User, db

def init_auth_routes(app):
    @app.route('/')
    def home():
        if "username" in session:
            return redirect(url_for('dashboard'))
        elif request.cookies.get('remember_me'):
            session['username'] = request.cookies.get('remember_me')
            return redirect(url_for('dashboard'))
        
        return render_template('login.html')

    @app.route('/login', methods=['GET', 'POST']) 
    def login():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            remember_me = request.form.get('remember_me')


            user = User.query.filter_by(username=username).first()
            
            if user and user.check_password(password):
                session['username'] = user.username
                response = redirect('/dashboard')
                if remember_me:
                    response.set_cookie('remember_me', user.username, max_age=30*24*60*60)
                return response
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
            profile_image = request.files.get('profile_image')

            existing_user = User.query.filter((User.email == email) | (User.username == username)).first()
            if existing_user:
                return render_template('register.html', error="Email or Username already exists!")

            image_filename = 'default.png'
            if profile_image and allowed_file(profile_image.filename):
                image_filename = secure_filename(profile_image.filename)
                profile_image.save(os.path.join(app.config['UPLOAD_FOLDER'], image_filename))

            new_user = User(nom=nom, prenom=prenom, username=username, email=email, genre=genre, password=password)
            new_user.image = image_filename
            db.session.add(new_user)
            db.session.commit()
            return redirect('/login')

        return render_template('register.html')

    def allowed_file(filename):
        allowed_extensions = {'png', 'jpg', 'jpeg', 'gif'}
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

    @app.route('/upload_image', methods=['POST'])
    def upload_image():
        if 'username' not in session:
            return redirect(url_for('login'))
        
        file = request.files.get('profile_image')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            user = User.query.filter_by(username=session['username']).first()
            user.image = filename
            flash('Profile image updated successfully!', 'success')
        else:
            flash('Invalid file type or no file uploaded.', 'danger')
        return redirect(url_for('dashboard'))

    @app.route('/dashboard')
    def dashboard():
        if 'username' in session:
            user = User.query.filter_by(username=session['username']).first()
            if user:
                user.image = user.image if hasattr(user, 'image') else 'default.png'
                return render_template('dashboard.html', user=user)
        return redirect('/login') 

    @app.route('/logout')
    def logout():
        session.pop('username', None)
        response = redirect(url_for('login'))
        response.delete_cookie('remember_me')
        return response