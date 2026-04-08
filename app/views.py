import os
import cv2
import numpy as np
from flask import render_template, request, Blueprint
from flask_login import login_required, current_user
from models import db, Identity 
import matplotlib.image as matimg
from app.face_recognition import faceRecognitionPipeline

views_bp = Blueprint('views', __name__)

UPLOAD_FOLDER = 'static/upload'

# --- NO INDEX FUNCTION HERE ---

@views_bp.route('/methodology')
def methodology():
    return render_template('app.html')

@views_bp.route('/gender', methods=['GET', 'POST'])
@login_required 
def genderapp():
    if request.method == 'POST':
        f = request.files['image_name']
        path = os.path.join(UPLOAD_FOLDER, f.filename)
        f.save(path) 
        
        pred_image, predictions = faceRecognitionPipeline(path)
        cv2.imwrite('./static/predict/prediction_image.jpg', pred_image)
        
        report = []
        saved_identities = Identity.query.filter_by(user_id=current_user.id).all()

        for i, obj in enumerate(predictions):
            live_vector = obj['eig_img'].flatten()
            identity_name = "Unrecognized"
            
            if current_user.is_premium and saved_identities:
                min_dist = 1.5 
                for person in saved_identities:
                    try:
                        saved_vector = np.array(person.feature_vector.split(','), dtype=float)
                        dist = np.linalg.norm(live_vector - saved_vector)
                        if dist < min_dist:
                            min_dist = dist
                            identity_name = f"MATCH: {person.name}"
                    except Exception as e:
                        continue

            gender_name = obj['prediction_name'] 
            score = round(obj['score'] * 100, 2) 
            
            gray_name = f'roi_{i}.jpg'
            eig_name = f'eigen_{i}.jpg'
            matimg.imsave(f'./static/predict/{gray_name}', obj['roi'], cmap='gray')
            matimg.imsave(f'./static/predict/{eig_name}', obj['eig_img'].reshape(100, 100), cmap='gray')
            
            display_name = identity_name if current_user.is_premium and identity_name != "Unrecognized" else gender_name
            report.append([gray_name, eig_name, display_name, score])
            
        return render_template('gender.html', fileupload=True, report=report)
    
    return render_template('gender.html', fileupload=False)