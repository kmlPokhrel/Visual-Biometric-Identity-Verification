import os
from app.face_recognition import faceRecognitionPipeline
import stripe
from flask import Flask, render_template, redirect, url_for, flash, request, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_bcrypt import Bcrypt
from models import db, User, Identity # Added Identity
from app.views import views_bp
import numpy as np
from app.face_recognition import faceRecognitionPipeline
from dotenv import load_dotenv

app = Flask(__name__)

# --- CONFIGURATION ---
app.config['SECRET_KEY'] = 'your_secret_hack_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
load_dotenv()
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
# --- INITIALIZE ---
db.init_app(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

with app.app_context():
    db.create_all()

# --- STRIPE ROUTES ---

@app.route('/create-checkout-session', methods=['POST'])
@login_required
def create_checkout_session():
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{'price_data': {'currency': 'usd', 'product_data': {'name': 'Elite Biometric Access'}, 'unit_amount': 500}, 'quantity': 1}],
            mode='payment',
            success_url=url_for('payment_success', _external=True) + "?session_id={CHECKOUT_SESSION_ID}",
            cancel_url=url_for('dashboard', _external=True),
        )
        return redirect(session.url, code=303)
    except Exception as e:
        return str(e), 400

@app.route('/payment-success')
@login_required
def payment_success():
    current_user.is_premium = True
    db.session.commit()
    return render_template('success.html', user=current_user)

# --- AUTH ROUTES ---

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        hashed = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
        user = User(username=request.form['username'], password=hashed)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and bcrypt.check_password_hash(user.password, request.form['password']):
            login_user(user)
            return redirect(url_for('dashboard'))
        flash('Invalid Credentials')
    return render_template('login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.username)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

# --- BLUEPRINT ---
app.register_blueprint(views_bp)

@app.route('/enroll', methods=['GET', 'POST'])
@login_required
def enroll():
    if not current_user.is_premium:
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        name = request.form['name']
        f = request.files['image']
        temp_path = os.path.join('static/upload', 'enroll_temp.jpg')
        f.save(temp_path)
        
        _, predictions = faceRecognitionPipeline(temp_path)
        
        if predictions:
            vector = predictions[0]['eig_img'].flatten()
            
            # --- FIX: Use join to ensure NO numbers are skipped ---
            vector_str = ",".join(vector.astype(str))
            
            new_identity = Identity(name=name, feature_vector=vector_str, user_id=current_user.id)
            db.session.add(new_identity)
            db.session.commit()
            
            flash(f"Successfully enrolled {name}!")
            return redirect(url_for('dashboard'))
    return render_template('enroll.html')
@app.route('/analytics')
@login_required
def analytics():
    # Only Elite users get to see the technical reports
    if not current_user.is_premium:
        flash("Upgrade to Elite to view Forensic Analytics.")
        return redirect(url_for('dashboard'))
    return render_template('analytics.html')
@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)