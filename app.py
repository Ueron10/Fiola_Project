"""
Foundation Shade Predictor Web Interface
"""

import sys
from pathlib import Path
from flask import Flask, render_template, request, jsonify
import os
import base64
import cv2
import numpy as np

sys.path.append(str(Path(__file__).parent / "src"))

from predict import predict_from_image, predict_from_frame
from config import ALLOWED_EXTENSIONS

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if not allowed_file(file.filename):
        return jsonify({'error': 'File type not supported. Use JPG, PNG, WEBP, BMP, or TIFF'}), 400
    
    filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filename)
    
    try:
        result = predict_from_image(filename)
        
        if result is None:
            return jsonify({'error': 'Failed to process image. Make sure face is clearly visible.'}), 400
        
        os.remove(filename)
        
        return jsonify({
            'success': True,
            'skin_color': result['skin_color'],
            'foundation_shade': result['foundation_shade'],
            'confidence': result['confidence'],
            'rgb_values': result['rgb_values'],
            'model_type': result['model_type']
        })
        
    except Exception as e:
        if os.path.exists(filename):
            os.remove(filename)
        return jsonify({'error': f'Error processing image: {str(e)}'}), 500

@app.route('/predict_frame', methods=['POST'])
def predict_frame():
    try:
        data = request.get_json()
        if not data or 'frame' not in data:
            return jsonify({'error': 'No frame data provided'}), 400
        
        frame_data = data['frame']
        if ',' in frame_data:
            frame_data = frame_data.split(',')[1]
        
        frame_bytes = base64.b64decode(frame_data)
        nparr = np.frombuffer(frame_bytes, np.uint8)
        frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        if frame is None:
            return jsonify({'error': 'Failed to decode frame'}), 400
        
        result = predict_from_frame(frame)
        
        if result is None:
            return jsonify({'error': 'Failed to process frame'}), 400
        
        return jsonify({
            'success': True,
            'skin_color': result['skin_color'],
            'foundation_shade': result['foundation_shade'],
            'confidence': result['confidence'],
            'rgb_values': result['rgb_values'],
            'model_type': result['model_type']
        })
        
    except Exception as e:
        return jsonify({'error': f'Error processing frame: {str(e)}'}), 500

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
