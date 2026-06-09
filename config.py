"""
Configuration file for Foundation Shade Predictor
YOLO-based skin tone detection and foundation recommendation
"""

from pathlib import Path

# Base paths
BASE_PATH = Path(__file__).parent
RAW_IMAGES_PATH = BASE_PATH / "raw_images"
MODELS_PATH = BASE_PATH / "models"
NOTEBOOKS_PATH = BASE_PATH / "notebooks"

# YOLO configuration
YOLO_MODEL_NAME = MODELS_PATH / 'yolov8n.pt'
YOLO_CONFIDENCE_THRESHOLD = 0.25

# Mapping skin color ke foundation shade
SKIN_TO_FOUNDATION = {
    'Fair': 'Porcelain',
    'Medium': 'Natural Beige',
    'Tan': 'Caramel'
}

# Supported image formats
SUPPORTED_FORMATS = {'.jpg', '.jpeg', '.png', '.webp', '.avif', '.bmp', '.tiff'}

# Allowed extensions for Flask upload
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'webp', 'bmp', 'tiff'}

# Dataset categories
CATEGORIES = ['fair', 'medium', 'tan']
