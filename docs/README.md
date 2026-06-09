# Foundation Shade Predictor

Aplikasi machine learning untuk memprediksi shade foundation yang tepat berdasarkan warna kulit dari foto menggunakan **YOLO (You Only Look Once)**.

## Fitur

- **Prediksi dari Foto**: Upload foto wajah untuk mendapatkan rekomendasi foundation shade
- **Real-time Camera Detection**: Kamera dengan deteksi wajah otomatis menggunakan TensorFlow.js dan COCO-SSD
- **Bounding Box Display**: Menampilkan kotak hijau di sekitar wajah yang terdeteksi
- **Auto-Capture**: Foto otomatis di-capture setelah 3 detik deteksi wajah berkelanjutan
- **YOLO Model**: Object detection untuk deteksi wajah yang cepat dan akurat
- **Deteksi Wajah Otomatis**: Menggunakan YOLO pre-trained model untuk mendeteksi area wajah
- **Color Analysis**: Analisis warna kulit berbasis RGB dan HSV untuk klasifikasi skin tone
- **3 Kategori Skin Tone**: Fair, Medium, Tan
- **Mapping Foundation**: 
  - Fair -> Porcelain
  - Medium -> Natural Beige  
  - Tan -> Caramel
- **Confidence Score**: Menampilkan tingkat kepercayaan prediksi
- **Web Interface**: Interface user-friendly dengan Flask
- **Dynamic Color Display**: Warna box hasil sesuai dengan rekomendasi foundation
- **RGB Values**: Menampilkan nilai RGB untuk referensi warna

## Struktur Project

```
DL/
|-- app.py                         # Flask web application
|-- requirements.txt               # Dependencies
|-- config.py                      # Konfigurasi project
|-- src/
|   |-- predict_foundation_yolo.py # Prediksi foundation shade dengan YOLO
|-- templates/
|   |-- index.html                 # Web interface dengan real-time camera detection
|-- raw_images/                    # Dataset images
|   |-- fair/
|   |-- medium/
|   |-- tan/
|-- uploads/                       # Temporary uploaded files
```

## Cara Penggunaan

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

**Dependencies Utama:**
- `ultralytics==8.0.196` - YOLO object detection
- `opencv-python==4.8.1.78` - Computer vision
- `flask==3.0.0` - Web interface
- `numpy==1.24.3` - Numerical computing
- `pandas==2.0.3` - Data manipulation
- `Pillow==10.0.0` - Image processing

### 2. Jalankan Web Interface

```bash
python app.py
```

Aplikasi akan berjalan di `http://localhost:5000`

### 3. Cara Penggunaan Web App

**Upload Foto:**
1. Buka browser dan akses `http://localhost:5000`
2. Upload foto wajah yang jelas atau drag & drop
3. Klik tombol "Prediksi Foundation Shade"
4. Lihat hasil rekomendasi foundation dengan warna yang sesuai

**Kamera dengan Auto-Detection:**
1. Klik tombol "Buka Kamera"
2. Berikan izin kamera saat browser meminta
3. Sistem akan mendeteksi wajah secara real-time dengan bounding box hijau
4. Setelah 3 detik deteksi berkelanjutan, foto otomatis di-capture
5. Atau klik "Capture Foto" untuk capture manual
6. Hasil prediksi akan ditampilkan otomatis

### 4. Command Line Usage

```bash
# Prediksi dari file foto
python src/predict_foundation_yolo.py "path/to/image.jpg"
```

## Persyaratan Foto

- **Format**: JPG, PNG, WEBP, BMP, TIFF
- **Kualitas**: Wajah terlihat jelas
- **Pencahayaan**: Cahaya yang baik, tidak terlalu gelap atau terang
- **Posisi**: Foto frontal (menghadap kamera)
- **Filter**: Hindari filter berlebihan

## Technical Details

### Real-time Camera Detection (Frontend)
1. **TensorFlow.js**: Library machine learning untuk browser
2. **COCO-SSD Model**: Pre-trained model untuk deteksi objek real-time
3. **Canvas Overlay**: Menampilkan bounding box hijau di sekitar wajah terdeteksi
4. **Auto-Capture Logic**: Capture otomatis setelah 3 detik deteksi berkelanjutan
5. **Countdown Timer**: Menampilkan hitung mundur saat wajah terdeteksi

### YOLO Pipeline (Backend)
1. **Face Detection**: YOLO pre-trained model untuk deteksi wajah real-time
2. **Face Extraction**: Crop area wajah dari bounding box YOLO
3. **Color Analysis**: Konversi RGB dan HSV untuk analisis warna kulit
4. **Skin Tone Classification**: Klasifikasi berdasarkan threshold RGB dan HSV
5. **Foundation Mapping**: Skin tone ke foundation shade
6. **RGB Display**: Menampilkan nilai RGB untuk referensi warna

## Hasil Prediksi

Contoh output:

```
============================================================
FOUNDATION SHADE RECOMMENDATION (YOLO)
============================================================
Image: sample.jpg
Model: YOLO
RGB Values: (210, 180, 150)
Detected Skin Type: Fair
Recommended Foundation: Porcelain

Confidence:
   Fair: 94.2% <-
   Medium: 4.1%
   Tan: 1.7%
============================================================
```

## Troubleshooting

### "Tidak ada wajah terdeteksi"
- Pastikan wajah terlihat jelas di foto
- Coba dengan pencahayaan yang lebih baik
- Hindari foto samping atau posisi miring
- Pastikan foto menampilkan orang (bukan objek lain)

### "Format tidak didukung"
- Gunakan format: JPG, PNG, WEBP, BMP, TIFF
- AVIF tidak didukung oleh OpenCV

### "Error loading YOLO model"
- Pastikan koneksi internet aktif untuk download model pertama kali
- YOLO akan otomatis download model jika belum ada
- Cek apakah ultralytics terinstall dengan benar

### "Kamera tidak dapat diakses"
- Pastikan mengakses via `http://localhost:5000` atau `http://127.0.0.1:5000`
- Browser memerlukan HTTPS untuk kamera pada non-localhost
- Berikan izin kamera saat browser meminta
- Pastikan kamera tidak sedang digunakan aplikasi lain

## Dataset Requirements

### Struktur Folder
```
raw_images/
  fair/
    image1.jpg
    image2.jpg
    ...
  medium/
    image1.jpg
    image2.jpg
    ...
  tan/
    image1.jpg
    image2.jpg
    ...
```

### Rekomendasi Dataset
- **Minimal**: 50 gambar per kategori
- **Optimal**: 100+ gambar per kategori
- **Variasi**: Berbagai pencahayaan, angle, dan usia
- **Kualitas**: High resolution, wajah jelas

## Kontribusi

1. Fork project
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create Pull Request

## License

MIT License - feel free to use this project for learning and development purposes.

---

**Versi**: 3.0  
**Status**: Production Ready  
**Last Updated**: Juni 2026
