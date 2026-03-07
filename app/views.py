import os
import cv2
from app.face_recognition import faceRecognitionPipeline
from flask import render_template, request, Blueprint
import matplotlib.image as matimg

# Create the Blueprint
views_bp = Blueprint('views', __name__)

UPLOAD_FOLDER = 'static/upload'

@views_bp.route('/')
def index():
    return render_template('index.html')

@views_bp.route('/methodology')
def methodology():
    return render_template('app.html')

@views_bp.route('/gender', methods=['GET', 'POST'])
def genderapp():
    if request.method == 'POST':
        f = request.files['image_name']
        filename = f.filename
        path = os.path.join(UPLOAD_FOLDER, filename)
        f.save(path) 
        
        # Process image and save prediction
        pred_image, predictions = faceRecognitionPipeline(path)
        pred_filename = 'prediction_image.jpg'
        cv2.imwrite(f'./static/predict/{pred_filename}', pred_image)
        
        report = []
        for i, obj in enumerate(predictions):
            gray_image = obj['roi'] 
            eigen_image = obj['eig_img'].reshape(100, 100) 
            gender_name = obj['prediction_name'] 
            score = round(obj['score'] * 100, 2) 
            
            # Save technical assets for the dashboard
            gray_image_name = f'roi_{i}.jpg'
            eig_image_name = f'eigen_{i}.jpg'
            matimg.imsave(f'./static/predict/{gray_image_name}', gray_image, cmap='gray')
            matimg.imsave(f'./static/predict/{eig_image_name}', eigen_image, cmap='gray')
            
            report.append([gray_image_name, eig_image_name, gender_name, score])
            
        return render_template('gender.html', fileupload=True, report=report)
    
    return render_template('gender.html', fileupload=False)