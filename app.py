"""
Foundation Shade Predictor Web Interface
Upload photo untuk mendapatkan rekomendasi foundation shade
"""

import sys
from pathlib import Path
from flask import Flask, render_template, request, jsonify
import os

# Add src directory to path
sys.path.append(str(Path(__file__).parent / "src"))

from predict import predict_from_image
from config import ALLOWED_EXTENSIONS

app = Flask(__name__)

# Flask configuration
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Create upload directory if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    """Check if file has allowed extension"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    """Render main page"""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Handle image upload and prediction"""
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if not allowed_file(file.filename):
        return jsonify({'error': 'File type not supported. Use JPG, PNG, WEBP, BMP, or TIFF'}), 400
    
    # Save uploaded file
    filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filename)
    
    try:
        # Make prediction
        result = predict_from_image(filename)
        
        if result is None:
            return jsonify({'error': 'Failed to process image. Make sure face is clearly visible.'}), 400
        
        # Clean up uploaded file
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
        # Clean up uploaded file if error occurs
        if os.path.exists(filename):
            os.remove(filename)
        return jsonify({'error': f'Error processing image: {str(e)}'}), 500

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    # Run on localhost for camera access (browsers require HTTPS for camera on non-localhost)
    # Use host='0.0.0.0' only if you need network access and have HTTPS configured
    app.run(debug=True, host='127.0.0.1', port=5000)
