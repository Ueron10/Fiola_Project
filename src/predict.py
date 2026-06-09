"""
Foundation Shade Predictor using YOLO
YOLO-based face detection and skin tone classification
"""

import cv2
import numpy as np
from pathlib import Path
from ultralytics import YOLO
import sys

# Add parent directory to path for config
sys.path.append(str(Path(__file__).parent.parent))
from config import *

def load_yolo_model():
    """Load YOLO model for face detection"""
    try:
        model = YOLO(YOLO_MODEL_NAME)
        print(f"YOLO model loaded successfully: {YOLO_MODEL_NAME}")
        return model
    except Exception as e:
        print(f"Error loading YOLO model: {e}")
        print("Attempting to download YOLO model...")
        try:
            model = YOLO(YOLO_MODEL_NAME)
            print(f"YOLO model downloaded and loaded successfully: {YOLO_MODEL_NAME}")
            return model
        except Exception as e2:
            print(f"Error downloading YOLO model: {e2}")
            return None

def analyze_skin_tone(face_region):
    """Analyze skin tone from face region using color analysis"""
    try:
        face_rgb = cv2.cvtColor(face_region, cv2.COLOR_BGR2RGB)
        pixels = face_rgb.reshape(-1, 3)
        
        brightness = np.mean(pixels, axis=1)
        valid_pixels = pixels[(brightness > 20) & (brightness < 250)]
        
        if len(valid_pixels) == 0:
            valid_pixels = pixels
            print("Warning: Using all pixels due to filtering")
        
        mean_rgb = np.mean(valid_pixels, axis=0)
        r, g, b = mean_rgb
        
        print(f"Mean RGB - R: {r:.1f}, G: {g:.1f}, B: {b:.1f}")
        
        face_hsv = cv2.cvtColor(face_region, cv2.COLOR_BGR2HSV)
        mean_hsv = np.mean(face_hsv.reshape(-1, 3), axis=0)
        h, s, v = mean_hsv
        
        if r > 160 and g > 120 and b > 100 and s < 50:
            print("Classified as: Fair")
            return 'Fair', (int(r), int(g), int(b))
        elif r > 120 and g > 90 and b > 70 and s < 100:
            print("Classified as: Medium")
            return 'Medium', (int(r), int(g), int(b))
        else:
            print("Classified as: Tan")
            return 'Tan', (int(r), int(g), int(b))
    except Exception as e:
        print(f"Error analyzing skin tone: {e}")
        return 'Medium', (150, 120, 100)

def calculate_confidence(skin_tone, rgb_values):
    """Calculate confidence scores for each skin tone class"""
    r, g, b = rgb_values
    
    typical_values = {
        'Fair': (210, 180, 150),
        'Medium': (170, 140, 110),
        'Tan': (130, 100, 80)
    }
    
    distances = {}
    for tone, typical in typical_values.items():
        dist = np.sqrt(sum((a - b) ** 2 for a, b in zip(rgb_values, typical)))
        distances[tone] = dist
    
    max_dist = max(distances.values())
    confidence = {}
    for tone, dist in distances.items():
        conf = 1 - (dist / (max_dist * 1.5))
        confidence[tone] = max(0, min(1, conf))
    
    total = sum(confidence.values())
    if total > 0:
        confidence = {k: v/total for k, v in confidence.items()}
    
    return confidence

def detect_face_with_yolo(image_path, model):
    """Detect face using YOLO model"""
    try:
        img = cv2.imread(str(image_path))
        if img is None:
            print(f"Gagal membaca gambar: {image_path}")
            return None
        
        results = model(img, conf=0.25)
        detections = results[0].boxes
        
        if len(detections) == 0:
            print(f"Tidak ada objek terdeteksi di gambar")
            return None
        
        person_detections = [box for box in detections if int(box.cls[0]) == 0]
        
        if len(person_detections) == 0:
            if len(detections) > 0:
                person_detections = detections
            else:
                return None
        
        largest_box = max(person_detections, key=lambda box: (box.xywh[0][2] * box.xywh[0][3]))
        x1, y1, x2, y2 = map(int, largest_box.xyxy[0])
        
        face_height = int((y2 - y1) * 0.5)
        face_y1 = y1
        face_y2 = y1 + face_height
        face_x1 = x1
        face_x2 = x2
        
        face_y1 = max(0, face_y1)
        face_y2 = min(img.shape[0], face_y2)
        face_x1 = max(0, face_x1)
        face_x2 = min(img.shape[1], face_x2)
        
        face_region = img[face_y1:face_y2, face_x1:face_x2]
        
        if face_region.size == 0:
            return None
        
        return face_region
    except Exception as e:
        print(f"Error saat mendeteksi wajah dengan YOLO: {e}")
        return None

def predict_from_image(image_path):
    """Predict skin tone using YOLO for face detection and color analysis"""
    print("=" * 60)
    print("MEMULAI PROSES PREDIKSI SKIN TONE")
    print("=" * 60)
    
    model = load_yolo_model()
    if model is None:
        print("Gagal memuat model YOLO")
        return None
    
    image_path = Path(image_path)
    
    if image_path.suffix.lower() not in SUPPORTED_FORMATS:
        print(f"Format tidak didukung: {image_path.suffix}")
        return None
    
    print(f"Memproses gambar: {image_path.name}")
    
    face_region = detect_face_with_yolo(image_path, model)
    if face_region is None:
        print("Gagal mendeteksi wajah")
        return None
    
    try:
        skin_tone, rgb_values = analyze_skin_tone(face_region)
        confidence = calculate_confidence(skin_tone, rgb_values)
        foundation = SKIN_TO_FOUNDATION.get(skin_tone, 'Unknown')
        
        result = {
            'skin_color': skin_tone,
            'foundation_shade': foundation,
            'confidence': confidence,
            'image': image_path.name,
            'model_type': 'YOLO',
            'rgb_values': rgb_values
        }
        
        print("=" * 60)
        print("HASIL PREDIKSI")
        print("=" * 60)
        print(f"Skin Tone Terdeteksi: {skin_tone}")
        print(f"RGB Values: {rgb_values}")
        print(f"Foundation Rekomendasi: {foundation}")
        print("=" * 60)
        
        return result
    except Exception as e:
        print(f"Error saat prediksi: {e}")
        return None
