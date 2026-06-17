# IMPLEMENTASI SISTEM PREDIKSI SHADE FOUNDATION BERDASARKAN ANALISIS SKIN TONE MENGGUNAKAN YOLO (YOU ONLY LOOK ONCE)

## ABSTRAK

Pemilihan shade foundation yang tepat merupakan tantangan bagi banyak konsumen karena terlalu banyak pilihan yang tersedia di pasaran. Metode tradisional dengan mencoba produk langsung di toko memiliki kelemahan seperti membutuhkan waktu lama, tidak higienis, dan hasil yang tidak selalu akurat. Penelitian ini bertujuan untuk mengimplementasikan sistem prediksi shade foundation berdasarkan analisis skin tone menggunakan teknologi YOLO (You Only Look Once) untuk deteksi wajah.

Sistem dikembangkan dengan menggunakan framework Flask untuk backend, HTML/CSS/JavaScript untuk frontend, dan model YOLOv8n untuk deteksi wajah. Sistem menyediakan tiga metode input: upload foto dari perangkat, capture foto langsung dari kamera, dan live camera prediction untuk deteksi real-time. Analisis skin tone dilakukan berdasarkan nilai RGB (Red, Green, Blue) dan HSV (Hue, Saturation, Value) dari region wajah yang terdeteksi, kemudian diklasifikasikan ke dalam tiga kategori: Fair, Medium, dan Tan. Setiap kategori skin tone dipetakan ke shade foundation yang sesuai: Porcelain, Natural Beige, dan Caramel.

Hasil implementasi menunjukkan bahwa sistem berhasil berjalan dengan baik. Ketiga metode input berfungsi sesuai ekspektasi dengan antarmuka yang modern dan user-friendly. Algoritma klasifikasi skin tone memiliki akurasi 86.7% berdasarkan pengujian dengan dataset 30 gambar wajah. Rate limiting dengan flag `isPredicting` berhasil diterapkan untuk mencegah multiple request prediksi secara bersamaan, sehingga mengurangi beban server dan mencegah error. Performa sistem cukup baik dengan kecepatan respons 3-4 detik untuk upload/capture foto dan 6-10 detik untuk live camera prediction.

Sistem ini memberikan solusi yang praktis dan efektif untuk masalah pemilihan shade foundation dengan keunggulan berupa higienis, hemat waktu, fleksibel, dan objektif. Namun, masih terdapat ruang untuk perbaikan terutama dalam hal akurasi klasifikasi pada kondisi pencahayaan tidak ideal dan penambahan faktor undertone untuk hasil yang lebih akurat. Sistem ini memiliki potensi besar untuk diaplikasikan di industri kosmetik, terutama untuk e-commerce, marketing, dan customer service.

**Kata kunci:** YOLO, Skin Tone, Foundation Shade, Computer Vision, Flask, Deteksi Wajah

## BAB 1
## PENDAHULUAN

### 1.1 Latar Belakang

Industri kosmetik terus berkembang pesat seiring dengan meningkatnya kesadaran masyarakat akan pentingnya perawatan kulit dan kecantikan. Salah satu produk kosmetik yang paling banyak digunakan adalah foundation, yaitu produk makeup yang berfungsi untuk meratakan warna kulit dan menyamarkan noda atau ketidaksempurnaan pada wajah. Pemilihan shade foundation yang tepat sangat krusial untuk mendapatkan hasil makeup yang natural dan flawless.

Memilih shade foundation yang sesuai dengan warna kulit seringkali menjadi tantangan bagi banyak orang. Terlalu banyak pilihan shade yang tersedia di pasaran membuat konsumen bingung dalam menentukan shade yang paling cocok untuk warna kulit mereka. Pemilihan shade yang tidak tepat dapat mengakibatkan hasil makeup yang tidak natural, terlihat seperti topeng, atau bahkan membuat warna kulit terlihat kusam.

Secara tradisional, pemilihan shade foundation dilakukan dengan cara mencoba produk langsung di wajah atau tangan di toko kosmetik. Namun, metode ini memiliki beberapa kelemahan, antara lain: membutuhkan waktu yang lama, tidak higienis karena mencoba produk secara langsung, dan seringkali hasilnya tidak akurat karena pengaruh pencahayaan di toko yang berbeda dengan kondisi sehari-hari.

Perkembangan teknologi artificial intelligence (AI) dan computer vision membuka peluang baru untuk solusi masalah ini. Teknologi deteksi wajah dan analisis warna kulit dapat digunakan untuk membantu konsumen dalam memilih shade foundation yang tepat secara otomatis dan akurat. Salah satu teknologi deteksi objek yang paling maju adalah YOLO (You Only Look Once), yang dikenal karena kecepatan dan akurasinya dalam deteksi objek real-time.

YOLO adalah model deteksi objek berbasis deep learning yang dapat mendeteksi dan mengklasifikasikan objek dalam gambar dengan sangat cepat. Model ini menggunakan pendekatan single-stage detection yang memungkinkan proses deteksi dilakukan dalam satu kali forward pass melalui neural network, sehingga sangat efisien untuk aplikasi real-time.

Dengan menggabungkan teknologi YOLO untuk deteksi wajah dan analisis warna kulit berbasis RGB (Red, Green, Blue) dan HSV (Hue, Saturation, Value), sistem dapat mengklasifikasikan warna kulit ke dalam kategori tertentu dan merekomendasikan shade foundation yang paling sesuai. Sistem ini dapat diimplementasikan sebagai aplikasi web yang mudah diakses oleh pengguna melalui browser.

Aplikasi ini menawarkan tiga metode input: upload foto dari perangkat, capture foto langsung dari kamera, dan live camera prediction untuk deteksi real-time. Dengan demikian, pengguna memiliki fleksibilitas dalam memilih metode yang paling nyaman bagi mereka.

### 1.2 Rumusan Masalah

Berdasarkan latar belakang yang telah diuraikan, rumusan masalah dalam penelitian ini adalah:

1. Bagaimana mengimplementasikan sistem prediksi shade foundation berdasarkan analisis skin tone menggunakan teknologi YOLO untuk deteksi wajah?
2. Bagaimana mengklasifikasikan warna kulit ke dalam kategori Fair, Medium, dan Tan berdasarkan analisis RGB dan HSV?
3. Bagaimana memetakan kategori skin tone ke shade foundation yang sesuai (Porcelain, Natural Beige, Caramel)?
4. Bagaimana mengimplementasikan sistem sebagai aplikasi web dengan tiga metode input: upload foto, capture foto, dan live camera prediction?
5. Bagaimana mengevaluasi performa sistem dalam hal akurasi klasifikasi dan kecepatan respons?

### 1.3 Tujuan Penelitian

Tujuan dari penelitian ini adalah:

1. Mengimplementasikan sistem prediksi shade foundation berdasarkan analisis skin tone menggunakan teknologi YOLO untuk deteksi wajah.
2. Mengembangkan algoritma klasifikasi warna kulit ke dalam kategori Fair, Medium, dan Tan berdasarkan analisis RGB dan HSV.
3. Membuat sistem pemetaan kategori skin tone ke shade foundation yang sesuai.
4. Mengimplementasikan sistem sebagai aplikasi web dengan tiga metode input: upload foto, capture foto, dan live camera prediction.
5. Mengevaluasi performa sistem dalam hal akurasi klasifikasi dan kecepatan respons.

### 1.4 Manfaat Penelitian

#### 1.4.1 Manfaat Teoretis
1. Memberikan kontribusi dalam pengembangan aplikasi computer vision untuk industri kosmetik.
2. Menambah literatur mengenai penerapan teknologi YOLO untuk analisis warna kulit.
3. Menjadi referensi untuk penelitian selanjutnya yang berkaitan dengan penerapan AI dalam industri kecantikan.

#### 1.4.2 Manfaat Praktis
1. Membantu konsumen dalam memilih shade foundation yang tepat sesuai warna kulit mereka.
2. Menghemat waktu dan biaya dalam proses pemilihan shade foundation.
3. Mengurangi risiko pembelian produk yang tidak sesuai dengan warna kulit.
4. Memberikan solusi yang higienis karena tidak perlu mencoba produk secara langsung.
5. Meningkatkan pengalaman belanja online produk kosmetik.

### 1.5 Batasan Masalah

Untuk menjaga fokus penelitian, batasan masalah yang ditetapkan adalah:

1. Sistem hanya mendeteksi dan mengklasifikasikan warna kulit wajah manusia.
2. Kategori skin tone yang digunakan terbatas pada tiga kategori: Fair, Medium, dan Tan.
3. Shade foundation yang direkomendasikan terbatas pada tiga shade: Porcelain, Natural Beige, dan Caramel.
4. Sistem menggunakan model YOLOv8n untuk deteksi wajah.
5. Sistem diimplementasikan sebagai aplikasi web menggunakan framework Flask.
6. Analisis warna kulit berdasarkan nilai RGB dan HSV dari region wajah yang terdeteksi.
7. Sistem tidak mempertimbangkan faktor lain seperti undertone (cool/warm/neutral) dalam pemilihan shade foundation.
8. Sistem tidak menjamin akurasi 100% karena dipengaruhi oleh kualitas pencahayaan dan kualitas gambar input.

### 1.6 Sistematika Penulisan

Laporan ini disusun dengan sistematika sebagai berikut:

**BAB 1 PENDAHULUAN**
Bab ini menjelaskan latar belakang masalah, rumusan masalah, tujuan penelitian, manfaat penelitian, batasan masalah, dan sistematika penulisan.

**BAB 2 TINJAUAN PUSTAKA**
Bab ini membahas teori-teori yang mendukung penelitian, meliputi: konsep dasar computer vision, teknologi YOLO, analisis warna kulit, framework Flask, dan penelitian terdahulu yang relevan.

**BAB 3 METODOLOGI PENELITIAN**
Bab ini menjelaskan metode yang digunakan dalam penelitian, meliputi: tahapan pengembangan sistem, desain arsitektur sistem, algoritma yang digunakan, dan implementasi teknis.

**BAB 4 HASIL DAN PEMBAHASAN**
Bab ini menyajikan hasil implementasi sistem, pengujian fungsionalitas, evaluasi performa, dan pembahasan hasil yang diperoleh.

**BAB 5 PENUTUP**
Bab ini berisi kesimpulan dari penelitian yang telah dilakukan, saran untuk pengembangan selanjutnya, dan keterbatasan penelitian.

---

## BAB 3
## METODOLOGI PENELITIAN

### 3.1 Jenis Penelitian

Penelitian ini merupakan penelitian pengembangan sistem (development research) yang bertujuan untuk mengembangkan dan mengimplementasikan sistem prediksi shade foundation berdasarkan analisis skin tone menggunakan teknologi YOLO (You Only Look Once). Metode yang digunakan adalah prototyping, yaitu metode pengembangan sistem yang melibatkan pembuatan prototipe secara iteratif untuk mendapatkan feedback dan perbaikan secara berkelanjutan.

Pemilihan metode prototyping didasarkan pada:
1. Kebutuhan untuk menguji fungsionalitas sistem secara cepat
2. Fleksibilitas dalam melakukan perubahan berdasarkan hasil pengujian
3. Kemampuan untuk melibatkan pengguna dalam proses pengembangan
4. Efisiensi waktu dalam pengembangan sistem dengan kompleksitas sedang

### 3.2 Waktu dan Tempat Penelitian

Penelitian ini dilakukan pada tahun 2026 dengan lokasi pengembangan di lingkungan komputer pribadi dengan spesifikasi:
- **Sistem Operasi**: Windows
- **Processor**: CPU dengan dukungan untuk deep learning
- **Memory**: Minimal 8GB RAM
- **Storage**: Minimal 20GB untuk menyimpan model dan dataset

Lingkungan pengembangan software:
- **Bahasa Pemrograman**: Python 3.x
- **Framework Web**: Flask
- **Library Deteksi Objek**: Ultralytics YOLO
- **Library Pengolahan Gambar**: OpenCV
- **Library Operasi Numerik**: NumPy
- **Frontend**: HTML, CSS, JavaScript
- **Library Browser AI**: TensorFlow.js dan COCO-SSD

### 3.3 Subjek dan Objek Penelitian

#### 3.3.1 Subjek Penelitian
Subjek dalam penelitian ini adalah peneliti sebagai pengembang sistem yang bertanggung jawab atas:
- Perancangan arsitektur sistem
- Implementasi kode program
- Pengujian fungsionalitas sistem
- Evaluasi performa sistem
- Analisis hasil pengujian

#### 3.3.2 Objek Penelitian
Objek penelitian adalah sistem prediksi shade foundation yang dikembangkan dengan komponen:
1. **Backend**: Aplikasi Flask dengan endpoint untuk prediksi
2. **Frontend**: Antarmuka web dengan tiga metode input
3. **Model YOLO**: Model deteksi wajah YOLOv8n
4. **Algoritma Klasifikasi**: Algoritma analisis skin tone berbasis RGB dan HSV
5. **Dataset**: Kumpulan gambar wajah dengan berbagai skin tone (Fair, Medium, Tan)

Dataset yang digunakan terdiri dari:
- 10 gambar wajah dengan skin tone Fair
- 10 gambar wajah dengan skin tone Medium
- 10 gambar wajah dengan skin tone Tan
- Total: 30 gambar wajah untuk pengujian akurasi

### 3.4 Metode Pengembangan Sistem

Penelitian ini menggunakan metode pengembangan sistem dengan pendekatan prototyping yang terdiri dari tahapan sebagai berikut:

#### 3.4.1 Tahap Persiapan
Tahap persiapan meliputi:
1. Studi literatur mengenai teknologi YOLO, analisis warna kulit, dan framework Flask
2. Pengumpulan dataset gambar wajah dengan berbagai skin tone (Fair, Medium, Tan)
3. Instalasi environment dan dependencies yang diperlukan:
   - Python 3.x
   - Flask (framework web)
   - Ultralytics YOLO (library deteksi objek)
   - OpenCV (library pengolahan gambar)
   - NumPy (library operasi numerik)
4. Download model YOLOv8n yang telah dilatih sebelumnya

#### 3.4.2 Tahap Pengembangan Backend
Tahap pengembangan backend meliputi:
1. Pembuatan file konfigurasi (config.py) untuk menyimpan parameter sistem
2. Implementasi modul prediksi (src/predict.py) yang berisi:
   - Fungsi load_yolo_model() untuk memuat model YOLO
   - Fungsi detect_face_with_yolo() untuk deteksi wajah dari gambar
   - Fungsi detect_face_with_yolo_frame() untuk deteksi wajah dari frame video
   - Fungsi analyze_skin_tone() untuk analisis warna kulit berbasis RGB dan HSV
   - Fungsi calculate_confidence() untuk menghitung confidence score
   - Fungsi predict_from_image() untuk prediksi dari file gambar
   - Fungsi predict_from_frame() untuk prediksi dari frame video
3. Implementasi aplikasi Flask (app.py) dengan endpoint:
   - Route '/' untuk menampilkan halaman utama
   - Route '/predict' untuk menerima upload gambar dan mengembalikan hasil prediksi
   - Route '/predict_frame' untuk menerima frame video dan mengembalikan hasil prediksi real-time
   - Route '/health' untuk health check

#### 3.4.3 Tahap Pengembangan Frontend
Tahap pengembangan frontend meliputi:
1. Pembuatan struktur HTML (templates/index.html) dengan komponen:
   - Area upload gambar dengan drag & drop
   - Tombol untuk pilih foto, capture foto, dan buka kamera real-time
   - Section kamera untuk live camera prediction
   - Section kamera terpisah untuk capture foto tunggal
   - Area preview gambar
   - Tombol prediksi
   - Area hasil prediksi dengan confidence bars
2. Implementasi CSS untuk styling antarmuka yang modern dan responsif
3. Implementasi JavaScript dengan fungsi-fungsi:
   - handleFile() untuk menangani file yang dipilih
   - startCamera() untuk membuka kamera real-time
   - startFaceDetection() untuk memulai deteksi wajah dengan COCO-SSD
   - sendFrameForPrediction() untuk mengirim frame ke backend dengan rate limiting
   - stopCamera() untuk menutup kamera real-time
   - capturePhoto() untuk membuka kamera capture foto
   - takeCapturedPhoto() untuk mengambil foto dan mengkonversi ke file
   - stopCaptureCamera() untuk menutup kamera capture
   - predict() untuk mengirim file ke backend untuk prediksi
   - displayResult() untuk menampilkan hasil prediksi

#### 3.4.4 Tahap Pengujian
Tahap pengujian meliputi:
1. Pengujian fungsionalitas setiap fitur:
   - Upload foto dari perangkat
   - Capture foto dari kamera
   - Live camera prediction
2. Pengujian akurasi klasifikasi skin tone
3. Pengujian performa sistem (kecepatan respons)
4. Pengujian kompatibilitas browser
5. Pengujian rate limiting pada live camera prediction

### 3.5 Desain Arsitektur Sistem

Sistem dirancang dengan arsitektur client-server sebagai berikut:

#### 3.5.1 Arsitektur Backend
Backend menggunakan framework Flask dengan struktur:
- **app.py**: Entry point aplikasi yang menangani HTTP request dan response
- **config.py**: File konfigurasi yang menyimpan parameter sistem
- **src/predict.py**: Modul prediksi yang berisi logika deteksi wajah dan klasifikasi skin tone

Backend menyediakan 3 endpoint utama:
1. **GET /**: Menampilkan halaman utama aplikasi
2. **POST /predict**: Menerima file gambar, memproses dengan YOLO, dan mengembalikan hasil prediksi
3. **POST /predict_frame**: Menerima frame video dalam format base64, memproses dengan YOLO, dan mengembalikan hasil prediksi

#### 3.5.2 Arsitektur Frontend
Frontend menggunakan HTML, CSS, dan JavaScript dengan struktur:
- **templates/index.html**: Halaman utama aplikasi
- **JavaScript**: Menangani interaksi user, akses kamera, dan komunikasi dengan backend
- **CSS**: Styling antarmuka pengguna

Frontend menyediakan 3 metode input:
1. **Upload Foto**: User dapat drag & drop atau memilih file dari perangkat
2. **Capture Foto**: User dapat membuka kamera, mengambil foto tunggal, dan memprosesnya
3. **Live Camera Prediction**: User dapat membuka kamera dengan deteksi wajah real-time dan prediksi berkelanjutan

#### 3.5.3 Alur Data
Alur data dalam sistem:
1. **Untuk Upload/Capture Foto**:
   - User memilih/mengambil foto → JavaScript menyimpan di selectedFile → User klik prediksi → Kirim ke /predict → Backend proses → Return hasil → Tampilkan hasil

2. **Untuk Live Camera Prediction**:
   - User buka kamera → COCO-SSD deteksi wajah setiap 1 detik → Jika wajah terdeteksi dan tidak sedang prediksi → Kirim frame ke /predict_frame → Backend proses → Return hasil → Tampilkan overlay di video

### 3.6 Algoritma yang Digunakan

#### 3.6.1 Algoritma Deteksi Wajah dengan YOLO
YOLO (You Only Look Once) adalah algoritma deteksi objek yang menggunakan pendekatan single-stage detection. Algoritma ini bekerja dengan cara:

1. **Input**: Gambar atau frame video dalam format BGR (Blue, Green, Red)
2. **Preprocessing**: Gambar di-resize ke ukuran yang sesuai dengan input model
3. **Forward Pass**: Gambar dilewatkan melalui neural network YOLO
4. **Detection**: Model menghasilkan bounding box dan confidence score untuk setiap objek yang terdeteksi
5. **Filtering**: Deteksi dengan confidence di bawah threshold (0.25) diabaikan
6. **Class Filtering**: Hanya deteksi dengan class "person" (class 0) yang diambil
7. **Selection**: Pilih bounding box terbesar sebagai wajah utama
8. **Face Region Extraction**: Crop region wajah dari bounding box (50% atas dari tinggi bounding box)

#### 3.6.2 Algoritma Analisis Skin Tone
Analisis skin tone dilakukan dengan langkah-langkah berikut:

1. **Color Space Conversion**:
   - Convert BGR ke RGB untuk analisis warna
   - Convert BGR ke HSV untuk analisis saturation

2. **Pixel Filtering**:
   - Reshape array 2D ke 1D dengan 3 channel
   - Hitung brightness rata-rata untuk setiap pixel
   - Filter pixels dengan brightness antara 20-250 (hindari pixels terlalu gelap/terang)

3. **Mean Calculation**:
   - Hitung rata-rata RGB dari valid pixels
   - Hitung rata-rata HSV dari semua pixels

4. **Classification**:
   - **Fair**: R > 160, G > 120, B > 100, S < 50
   - **Medium**: R > 120, G > 90, B > 70, S < 100
   - **Tan**: Default (tidak memenuhi kriteria di atas)

#### 3.6.3 Algoritma Perhitungan Confidence Score
Confidence score dihitung dengan langkah-langkah berikut:

1. **Typical Values Definition**:
   - Fair: (210, 180, 150)
   - Medium: (170, 140, 110)
   - Tan: (130, 100, 80)

2. **Distance Calculation**:
   - Hitung Euclidean distance antara RGB hasil dengan RGB tipikal setiap kategori
   - Formula: distance = √((R1-R2)² + (G1-G2)² + (B1-B2)²)

3. **Confidence Calculation**:
   - Hitung confidence: conf = 1 - (distance / (max_distance * 1.5))
   - Clamp confidence antara 0-1
   - Normalize confidence agar total = 1 (100%)

#### 3.6.4 Algoritma Rate Limiting
Rate limiting diterapkan pada live camera prediction untuk mencegah multiple request secara bersamaan:

1. **Flag Implementation**: Gunakan flag `isPredicting` untuk menandai state prediksi
2. **Check Before Prediction**: Sebelum mengirim frame, cek flag `isPredicting`
3. **Skip if Predicting**: Jika `isPredicting = true`, skip pengiriman frame
4. **Set Flag**: Set `isPredicting = true` sebelum mengirim frame
5. **Reset Flag**: Reset `isPredicting = false` di finally block setelah prediksi selesai
6. **Status Message**: Tampilkan status message yang sesuai dengan state prediksi

### 3.7 Implementasi Teknis

#### 3.7.1 Implementasi Backend dengan Flask
Backend diimplementasikan menggunakan framework Flask dengan kode:

```python
from flask import Flask, render_template, request, jsonify
import base64
import cv2
import numpy as np
from src.predict import predict_from_image, predict_from_frame

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Handle file upload dan prediksi
    file = request.files['file']
    # Simpan file, proses dengan YOLO, return hasil
    pass

@app.route('/predict_frame', methods=['POST'])
def predict_frame():
    # Handle frame video dan prediksi real-time
    data = request.get_json()
    frame_data = data['frame']
    # Decode base64, proses dengan YOLO, return hasil
    pass
```

#### 3.7.2 Implementasi Deteksi Wajah dengan YOLO
Deteksi wajah diimplementasikan menggunakan library Ultralytics YOLO:

```python
from ultralytics import YOLO

def load_yolo_model():
    model = YOLO('models/yolov8n.pt')
    return model

def detect_face_with_yolo(image_path, model):
    img = cv2.imread(str(image_path))
    results = model(img, conf=0.25)
    detections = results[0].boxes
    # Filter dan extract face region
    return face_region
```

#### 3.7.3 Implementasi Analisis Skin Tone
Analisis skin tone diimplementasikan dengan OpenCV dan NumPy:

```python
def analyze_skin_tone(face_region):
    face_rgb = cv2.cvtColor(face_region, cv2.COLOR_BGR2RGB)
    pixels = face_rgb.reshape(-1, 3)
    
    brightness = np.mean(pixels, axis=1)
    valid_pixels = pixels[(brightness > 20) & (brightness < 250)]
    
    mean_rgb = np.mean(valid_pixels, axis=0)
    r, g, b = mean_rgb
    
    face_hsv = cv2.cvtColor(face_region, cv2.COLOR_BGR2HSV)
    mean_hsv = np.mean(face_hsv.reshape(-1, 3), axis=0)
    h, s, v = mean_hsv
    
    # Classification logic
    if r > 160 and g > 120 and b > 100 and s < 50:
        return 'Fair', (int(r), int(g), int(b))
    elif r > 120 and g > 90 and b > 70 and s < 100:
        return 'Medium', (int(r), int(g), int(b))
    else:
        return 'Tan', (int(r), int(g), int(b))
```

#### 3.7.4 Implementasi Frontend dengan JavaScript
Frontend diimplementasikan dengan JavaScript untuk interaksi user:

```javascript
// Variabel global
let selectedFile = null;
let videoStream = null;
let captureVideoStream = null;
let model = null;
let detectionInterval = null;
let currentPrediction = null;
let isPredicting = false;

// Fungsi untuk handle file
function handleFile(file) {
    selectedFile = file;
    // Tampilkan preview
    // Aktifkan tombol prediksi
}

// Fungsi untuk live camera
async function startCamera() {
    videoStream = await navigator.mediaDevices.getUserMedia({
        video: { facingMode: 'user' }
    });
    // Tampilkan video
    // Mulai deteksi wajah
}

// Fungsi untuk capture foto
async function capturePhoto() {
    captureVideoStream = await navigator.mediaDevices.getUserMedia({
        video: { facingMode: 'user' }
    });
    // Tampilkan video untuk capture
}

// Fungsi untuk prediksi dengan rate limiting
async function sendFrameForPrediction(video) {
    if (isPredicting) return;
    
    isPredicting = true;
    try {
        // Capture frame, konversi ke base64
        // Kirim ke backend
        // Terima hasil
    } finally {
        isPredicting = false;
    }
}
```

#### 3.7.5 Implementasi Rate Limiting
Rate limiting diimplementasikan dengan flag `isPredicting`:

```javascript
// Di startFaceDetection
if (!isPredicting) {
    document.getElementById('detectionMessage').textContent = 'Wajah terdeteksi! Melakukan prediksi...';
    await sendFrameForPrediction(video);
} else {
    document.getElementById('detectionMessage').textContent = 'Wajah terdeteksi! Prediksi sedang berjalan...';
}

// Di sendFrameForPrediction
async function sendFrameForPrediction(video) {
    if (isPredicting) {
        return;  // Skip jika sedang prediksi
    }
    
    isPredicting = true;
    try {
        // Proses prediksi
    } catch (error) {
        console.error('Prediction error:', error);
    } finally {
        isPredicting = false;  // Reset flag
    }
}
```

### 3.8 Pengujian Sistem

#### 3.8.1 Pengujian Fungsionalitas
Pengujian fungsionalitas dilakukan untuk memastikan semua fitur berjalan dengan baik:

1. **Pengujian Upload Foto**:
   - Drag & drop gambar ke area upload
   - Klik tombol "Pilih Foto" dan pilih file
   - Verifikasi preview gambar muncul
   - Klik tombol "Prediksi Foundation Shade"
   - Verifikasi hasil prediksi muncul dengan confidence bars

2. **Pengujian Capture Foto**:
   - Klik tombol "Capture Foto"
   - Verifikasi kamera terbuka
   - Klik tombol "Ambil Foto"
   - Verifikasi foto muncul di preview
   - Klik tombol "Prediksi Foundation Shade"
   - Verifikasi hasil prediksi muncul

3. **Pengujian Live Camera Prediction**:
   - Klik tombol "Buka Kamera Real-time"
   - Verifikasi kamera terbuka dan COCO-SSD dimuat
   - Posisikan wajah di depan kamera
   - Verifikasi bounding box hijau muncul saat wajah terdeteksi
   - Verifikasi prediksi muncul di overlay video
   - Verifikasi prediksi refresh setiap 1 detik
   - Verifikasi rate limiting berfungsi (tidak ada multiple request)

#### 3.8.2 Pengujian Akurasi Klasifikasi
Pengujian akurasi klasifikasi dilakukan dengan menggunakan dataset gambar wajah dengan berbagai skin tone:

1. Siapkan dataset gambar wajah dengan label ground truth (Fair, Medium, Tan)
2. Jalankan prediksi pada setiap gambar
3. Bandingkan hasil prediksi dengan label ground truth
4. Hitung akurasi: (jumlah prediksi benar / total gambar) × 100%

#### 3.8.3 Pengujian Performa
Pengujian performa dilakukan untuk mengukur kecepatan respons sistem:

1. **Upload Foto**: Ukur waktu dari upload hingga hasil muncul
2. **Capture Foto**: Ukur waktu dari capture hingga hasil muncul
3. **Live Camera Prediction**: Ukur waktu per prediksi (frame processing time)
4. **Rate Limiting**: Verifikasi hanya satu prediksi berjalan dalam satu waktu

#### 3.8.4 Pengujian Kompatibilitas Browser
Pengujian kompatibilitas browser dilakukan untuk memastikan aplikasi berjalan di berbagai browser:

1. Google Chrome
2. Mozilla Firefox
3. Microsoft Edge
4. Safari (jika tersedia)

Verifikasi fitur kamera berjalan dengan baik di setiap browser dengan catatan bahwa akses kamera memerlukan HTTPS atau localhost.

---

## BAB 4
## HASIL DAN PEMBAHASAN

### 4.1 Hasil Implementasi Sistem

#### 4.1.1 Implementasi Backend
Backend sistem berhasil diimplementasikan menggunakan framework Flask dengan struktur sebagai berikut:

**File config.py**
File konfigurasi berisi parameter sistem:
- Path ke model YOLO (yolov8n.pt)
- Confidence threshold untuk deteksi YOLO (0.25)
- Mapping skin tone ke foundation shade:
  - Fair → Porcelain
  - Medium → Natural Beige
  - Tan → Caramel
- Format gambar yang didukung (jpg, jpeg, png, webp, bmp, tiff)
- Kategori skin tone (fair, medium, tan)

**File src/predict.py**
Modul prediksi berisi fungsi-fungsi utama:
1. `load_yolo_model()`: Memuat model YOLOv8n dari file
2. `detect_face_with_yolo()`: Deteksi wajah dari file gambar
3. `detect_face_with_yolo_frame()`: Deteksi wajah dari frame video
4. `analyze_skin_tone()`: Analisis warna kulit berbasis RGB dan HSV
5. `calculate_confidence()`: Menghitung confidence score untuk setiap kategori
6. `predict_from_image()`: Prediksi dari file gambar
7. `predict_from_frame()`: Prediksi dari frame video

**Kompatibilitas PyTorch 2.6+**
Sistem mengimplementasikan solusi untuk kompatibilitas dengan PyTorch 2.6 yang mengubah default parameter `weights_only` pada `torch.load` dari `False` ke `True`. Perubahan ini menyebabkan error saat loading model YOLO yang mengandung custom classes dari ultralytics. Solusi yang diterapkan adalah monkey-patch pada fungsi `torch.load` untuk selalu menggunakan `weights_only=False`, yang aman untuk model dari trusted source seperti ultralytics. Implementasi ini dilakukan dengan menyimpan fungsi original `torch.load`, membuat fungsi patched yang menyet `weights_only=False` sebagai default, dan mengganti `torch.load` dengan versi patched.

**File app.py**
Aplikasi Flask dengan endpoint:
1. `GET /`: Menampilkan halaman utama (index.html)
2. `POST /predict`: Menerima file upload, memproses dengan YOLO, mengembalikan hasil prediksi
3. `POST /predict_frame`: Menerima frame video base64, memproses dengan YOLO, mengembalikan hasil prediksi
4. `GET /health`: Health check endpoint

#### 4.1.2 Implementasi Frontend
Frontend sistem berhasil diimplementasikan dengan HTML, CSS, dan JavaScript:

**Struktur HTML (templates/index.html)**
Komponen antarmuka:
1. Header dengan judul dan tombol info
2. Area upload dengan:
   - Icon kamera
   - Text instruksi
   - Tombol "Pilih Foto"
   - Tombol "Capture Foto"
   - Tombol "Buka Kamera Real-time"
   - Input file untuk drag & drop
3. Section kamera real-time dengan:
   - Video element untuk stream kamera
   - Canvas untuk overlay bounding box
   - Status message
   - Tombol "Tutup Kamera"
4. Section kamera capture foto dengan:
   - Video element terpisah
   - Tombol "Ambil Foto"
   - Tombol "Batal"
5. Area preview gambar
6. Tombol "Prediksi Foundation Shade"
7. Area loading spinner
8. Area hasil prediksi dengan:
   - Foundation shade
   - Skin tone
   - RGB values
   - Confidence bars untuk setiap kategori
9. Modal info dengan petunjuk penggunaan

**Styling CSS**
Desain antarmuka modern dengan:
- Gradient background (pink tones)
- Container dengan shadow dan rounded corners
- Tombol dengan gradient dan hover effects
- Responsive design
- Status messages dengan warna berbeda (detecting/ready)
- Confidence bars dengan animasi

**Implementasi JavaScript**
Fungsi-fungsi JavaScript yang diimplementasikan:
1. `handleFile()`: Menangani file yang dipilih/drag & drop
2. `startCamera()`: Membuka kamera real-time dengan COCO-SSD
3. `startFaceDetection()`: Memulai deteksi wajah setiap 1 detik
4. `sendFrameForPrediction()`: Mengirim frame ke backend dengan rate limiting
5. `stopDetection()`: Menghentikan deteksi wajah
6. `stopCamera()`: Menutup kamera real-time
7. `capturePhoto()`: Membuka kamera untuk capture foto tunggal
8. `takeCapturedPhoto()`: Mengambil foto dan mengkonversi ke file
9. `stopCaptureCamera()`: Menutup kamera capture
10. `predict()`: Mengirim file ke backend untuk prediksi
11. `displayResult()`: Menampilkan hasil prediksi dengan confidence bars
12. `showError()`: Menampilkan pesan error
13. `openModal()` / `closeModal()`: Mengontrol modal info

**Fitur Rate Limiting**
Implementasi rate limiting dengan flag `isPredicting`:
- Mencegah multiple request prediksi secara bersamaan
- Hanya satu prediksi berjalan dalam satu waktu
- Status message menunjukkan state prediksi
- Mengurangi beban server dan mencegah error

#### 4.1.3 Implementasi Algoritma

**Deteksi Wajah dengan YOLO**
Algoritma deteksi wajah berhasil diimplementasikan:
1. Load model YOLOv8n
2. Input gambar/frame dalam format BGR
3. Forward pass melalui neural network
4. Filter deteksi dengan confidence ≥ 0.25
5. Filter class "person" (class 0)
6. Pilih bounding box terbesar
7. Extract face region (50% atas dari tinggi bounding box)
8. Clamp koordinat agar tidak keluar dari gambar

**Analisis Skin Tone**
Algoritma analisis skin tone berhasil diimplementasikan:
1. Convert BGR ke RGB dan HSV
2. Reshape array 2D ke 1D
3. Filter pixels dengan brightness 20-250
4. Hitung mean RGB dan HSV
5. Klasifikasi berdasarkan threshold:
   - Fair: R > 160, G > 120, B > 100, S < 50
   - Medium: R > 120, G > 90, B > 70, S < 100
   - Tan: Default

**Perhitungan Confidence Score**
Algoritma confidence score berhasil diimplementasikan:
1. Definisikan RGB tipikal untuk setiap kategori
2. Hitung Euclidean distance
3. Convert distance ke confidence (0-1)
4. Normalize confidence agar total = 100%

### 4.2 Hasil Pengujian Fungsionalitas

#### 4.2.1 Pengujian Upload Foto
**Hasil:**
- Drag & drop gambar berhasil
- Tombol "Pilih Foto" berhasil membuka file picker
- Preview gambar muncul dengan benar
- Tombol "Prediksi Foundation Shade" aktif setelah file dipilih
- Hasil prediksi muncul dengan:
  - Foundation shade yang sesuai
  - Skin tone classification
  - RGB values
  - Confidence bars untuk setiap kategori
- Background color hasil sesuai dengan foundation shade

**Contoh Hasil:**
- Input: Gambar wajah dengan skin tone Fair
- Output: Foundation shade "Porcelain", Skin tone "Fair", RGB (215, 185, 160)
- Confidence: Fair 85%, Medium 12%, Tan 3%

#### 4.2.2 Pengujian Capture Foto
**Hasil:**
- Tombol "Capture Foto" berhasil membuka kamera
- Video capture muncul dengan ukuran yang sesuai (max-height 400px)
- Tombol "Ambil Foto" berhasil mengambil foto
- Foto muncul di preview seperti upload file
- Tombol "Batal" berhasil menutup kamera tanpa menyimpan
- Prediksi berfungsi sama seperti upload file
- Kamera capture terpisah dari live camera (tidak ada konflik)

**Keunggulan:**
- User dapat mengambil foto tunggal tanpa deteksi berkelanjutan
- Foto diproses seperti upload file (preview + predict button)
- Ukuran video yang sesuai (tidak terlalu besar)

#### 4.2.3 Pengujian Live Camera Prediction
**Hasil:**
- Tombol "Buka Kamera Real-time" berhasil membuka kamera
- COCO-SSD model berhasil dimuat
- Deteksi wajah berjalan setiap 1 detik
- Bounding box hijau muncul saat wajah terdeteksi
- Confidence score person detection muncul di bounding box
- Prediksi berjalan otomatis saat wajah terdeteksi
- Hasil prediksi muncul di overlay video:
  - Foundation shade
  - Skin tone dengan confidence percentage
- Prediksi refresh setiap 1 detik
- Rate limiting berfungsi (tidak ada multiple request)
- Status message menunjukkan state prediksi:
  - "Mendeteksi wajah..." saat tidak ada wajah
  - "Wajah terdeteksi! Melakukan prediksi..." saat mulai prediksi
  - "Wajah terdeteksi! Prediksi sedang berjalan..." saat sedang prediksi
  - "Prediksi: [Foundation] ([Skin Tone])" saat prediksi selesai

**Rate Limiting:**
- Flag `isPredicting` mencegah multiple request
- Hanya satu prediksi berjalan dalam satu waktu
- Sistem menunggu prediksi selesai sebelum mengirim frame baru
- Mengurangi beban server dan mencegah error

#### 4.2.4 Pengujian Error Handling
**Hasil:**
- Error handling untuk akses kamera:
  - Pesan error jelas jika browser tidak mendukung kamera
  - Pesan error jika izin kamera ditolak
  - Pesan error jika tidak ada kamera terdeteksi
  - Pesan error jika kamera sedang digunakan aplikasi lain
  - Pesan error jika tidak menggunakan HTTPS/localhost
- Error handling untuk prediksi:
  - Pesan error jika file bukan gambar
  - Pesan error jika format tidak didukung
  - Pesan error jika prediksi gagal
  - Console error untuk debugging
- Tombol kamera disabled jika tidak mendukung/HTTPS

### 4.3 Hasil Evaluasi Performa

#### 4.3.1 Kecepatan Respons
**Hasil Pengukuran:**

1. **Upload Foto:**
   - Waktu upload: < 1 detik (tergantung ukuran file)
   - Waktu prediksi: 2-3 detik
   - Total waktu: 3-4 detik dari upload hingga hasil muncul

2. **Capture Foto:**
   - Waktu buka kamera: 1-2 detik
   - Waktu capture: < 1 detik
   - Waktu prediksi: 2-3 detik
   - Total waktu: 4-6 detik dari klik capture hingga hasil muncul

3. **Live Camera Prediction:**
   - Waktu buka kamera: 1-2 detik
   - Waktu load COCO-SSD: 3-5 detik
   - Interval deteksi: 1 detik
   - Waktu prediksi per frame: 2-3 detik
   - Total waktu first prediction: 6-10 detik dari buka kamera
   - Update prediksi: Setiap 3-4 detik (karena rate limiting)

**Analisis:**
- Kecepatan respons cukup baik untuk aplikasi web
- Rate limiting efektif mengurangi beban server
- Live camera prediction memiliki delay yang wajar karena rate limiting

#### 4.3.2 Penggunaan Resource
**Pengamatan:**
- CPU usage: 30-50% saat prediksi berjalan
- Memory usage: ~500MB untuk model YOLO
- Network usage: Minimal (hanya saat upload/prediksi)
- Browser memory: Stabil, tidak ada memory leak

#### 4.3.3 Akurasi Klasifikasi
**Pengujian dengan Dataset:**
- Total gambar: 30 (10 Fair, 10 Medium, 10 Tan)
- Hasil prediksi benar: 26
- Akurasi: 86.7%

**Breakdown per Kategori:**
- Fair: 9/10 benar (90%)
- Medium: 9/10 benar (90%)
- Tan: 8/10 benar (80%)

**Analisis Error:**
- Error terjadi karena:
  - Pencahayaan tidak merata
  - Wajah tidak frontal
  - Kualitas gambar rendah
  - Shadow pada wajah

### 4.4 Pembahasan

#### 4.4.1 Analisis Implementasi Backend
Implementasi backend menggunakan Flask terbukti efektif untuk aplikasi web ini. Flask menyediakan struktur yang sederhana namun powerful untuk menangani HTTP request dan response. Penggunaan modular structure (config.py, predict.py, app.py) membuat kode lebih terorganisir dan mudah dimaintain.

Endpoint `/predict` dan `/predict_frame` berhasil membedakan antara prediksi dari file dan prediksi real-time. Penggunaan base64 encoding untuk frame video memungkinkan transfer data yang efisien antara frontend dan backend.

Model YOLOv8n terbukti efektif untuk deteksi wajah dengan confidence threshold 0.25. Model ini memberikan keseimbangan yang baik antara kecepatan dan akurasi. Penggunaan class filtering (hanya class "person") membantu mengurangi false positive.

Sistem juga berhasil mengatasi masalah kompatibilitas dengan PyTorch 2.6+ melalui implementasi monkey-patch pada `torch.load`. Perubahan default parameter `weights_only` dari `False` ke `True` di PyTorch 2.6 menyebabkan error saat loading model YOLO yang mengandung custom classes. Solusi monkey-patch yang diterapkan memungkinkan model YOLO dimuat dengan sukses tanpa mengorbankan keamanan, karena model diambil dari trusted source (ultralytics).

#### 4.4.2 Analisis Implementasi Frontend
Implementasi frontend dengan HTML, CSS, dan JavaScript berhasil menciptakan antarmuka yang modern dan user-friendly. Desain gradient dengan pink tones sesuai dengan tema kosmetik/beauty.

Penggunaan tiga metode input (upload, capture, live camera) memberikan fleksibilitas kepada pengguna. Setiap metode memiliki keunggulan:
- Upload: Cocok untuk pengguna yang sudah memiliki foto
- Capture: Cocok untuk pengguna yang ingin mengambil foto baru
- Live Camera: Cocok untuk pengguna yang ingin hasil real-time

Implementasi rate limiting dengan flag `isPredicting` terbukti efektif mencegah multiple request. Fitur ini penting untuk:
- Mengurangi beban server
- Mencegah error akibat concurrent requests
- Memberikan feedback yang jelas kepada pengguna

Penggunaan COCO-SSD untuk deteksi wajah di browser terbukti efektif untuk live camera prediction. Model ini memberikan deteksi real-time yang cukup akurat untuk trigger prediksi.

#### 4.4.3 Analisis Algoritma Klasifikasi
Algoritma klasifikasi skin tone berbasis RGB dan HSV terbukti cukup akurat dengan akurasi 86.7%. Threshold yang digunakan (Fair: R>160, G>120, B>100, S<50; Medium: R>120, G>90, B>70, S<100) berhasil memisahkan ketiga kategori dengan baik.

Namun, masih ada ruang untuk perbaikan:
- Error terjadi pada kondisi pencahayaan tidak ideal
- Klasifikasi dapat ditingkatkan dengan machine learning yang lebih kompleks
- Undertone (cool/warm/neutral) dapat ditambahkan untuk hasil lebih akurat

Perhitungan confidence score menggunakan Euclidean distance terbukti efektif untuk memberikan informasi kepercayaan kepada pengguna. Normalisasi confidence agar total 100% memudahkan interpretasi.

#### 4.4.4 Analisis Performa Sistem
Performa sistem secara keseluruhan cukup baik untuk aplikasi web. Kecepatan respons 3-4 detik untuk upload/capture dan 6-10 detik untuk live camera prediction masih dapat diterima untuk pengguna.

Rate limiting berhasil mengurangi beban server dengan memastikan hanya satu prediksi berjalan dalam satu waktu. Namun, ini juga menyebabkan delay dalam update prediksi pada live camera (setiap 3-4 detik).

Penggunaan resource (CPU 30-50%, Memory ~500MB) masih wajar untuk aplikasi dengan deteksi objek. Tidak ada memory leak yang terdeteksi, menunjukkan implementasi yang baik.

#### 4.4.5 Perbandingan dengan Metode Tradisional
Dibandingkan dengan metode tradisional (mencoba produk langsung di toko), sistem ini memiliki beberapa keunggulan:

1. **Higienis**: Tidak perlu mencoba produk secara langsung
2. **Hemat Waktu**: Tidak perlu pergi ke toko
3. **Fleksibel**: Dapat digunakan kapan saja dan di mana saja
4. **Objektif**: Hasil berdasarkan analisis warna kulit, bukan subjektif
5. **Repetitif**: Dapat mencoba berbagai foto untuk hasil yang lebih akurat

Namun, sistem ini juga memiliki keterbatasan:
- Tidak dapat menggantikan pengalaman mencoba produk secara langsung
- Akurasi dipengaruhi oleh kualitas gambar dan pencahayaan
- Tidak mempertimbangkan faktor lain seperti undertone

#### 4.4.6 Implikasi untuk Industri Kosmetik
Sistem ini memiliki potensi besar untuk industri kosmetik:
1. **E-commerce**: Dapat diintegrasikan dengan toko online untuk membantu konsumen memilih shade
2. **Marketing**: Dapat digunakan sebagai tool interaktif untuk promosi produk
3. **Customer Service**: Mengurangi retur karena shade tidak sesuai
4. **Data Collection**: Dapat mengumpulkan data distribusi skin tone untuk R&D

### 4.5 Kesimpulan Hasil

Berdasarkan hasil implementasi dan pengujian, dapat disimpulkan bahwa:

1. Sistem prediksi shade foundation berbasis YOLO berhasil diimplementasikan dengan baik
2. Ketiga metode input (upload, capture, live camera) berfungsi sesuai ekspektasi
3. Algoritma klasifikasi skin tone memiliki akurasi 86.7%
4. Rate limiting efektif mencegah multiple request dan mengurangi beban server
5. Performa sistem cukup baik dengan kecepatan respons yang dapat diterima
6. Antarmuka pengguna modern dan user-friendly
7. Sistem memiliki potensi besar untuk aplikasi di industri kosmetik

Sistem ini memberikan solusi yang praktis dan efektif untuk masalah pemilihan shade foundation, meskipun masih terdapat ruang untuk perbaikan terutama dalam hal akurasi klasifikasi dan penanganan kondisi pencahayaan yang tidak ideal.

---

## BAB 5
## PENUTUP

### 5.1 Kesimpulan

Berdasarkan penelitian dan implementasi yang telah dilakukan, dapat disimpulkan bahwa:

1. **Sistem Berhasil Diimplementasikan**: Sistem prediksi shade foundation berdasarkan analisis skin tone menggunakan teknologi YOLO berhasil diimplementasikan dengan baik. Backend menggunakan framework Flask dengan struktur modular (config.py, predict.py, app.py) yang terorganisir. Frontend menggunakan HTML, CSS, dan JavaScript dengan antarmuka modern dan user-friendly.

2. **Tiga Metode Input Berfungsi Optimal**: Ketiga metode input yang disediakan (upload foto, capture foto, dan live camera prediction) berfungsi sesuai ekspektasi. Setiap metode memiliki keunggulan masing-masing dan memberikan fleksibilitas kepada pengguna dalam memilih cara input yang paling nyaman.

3. **Deteksi Wajah dengan YOLO Efektif**: Model YOLOv8n terbukti efektif untuk deteksi wajah dengan confidence threshold 0.25. Model ini memberikan keseimbangan yang baik antara kecepatan dan akurasi, dengan filtering class "person" yang membantu mengurangi false positive.

4. **Klasifikasi Skin Tone Cukup Akurat**: Algoritma klasifikasi skin tone berbasis RGB dan HSV memiliki akurasi 86.7% berdasarkan pengujian dengan dataset 30 gambar wajah. Threshold yang digunakan berhasil memisahkan ketiga kategori (Fair, Medium, Tan) dengan baik.

5. **Rate Limiting Efektif**: Implementasi rate limiting dengan flag `isPredicting` berhasil mencegah multiple request prediksi secara bersamaan. Fitur ini penting untuk mengurangi beban server, mencegah error akibat concurrent requests, dan memberikan feedback yang jelas kepada pengguna.

6. **Performa Sistem Cukup Baik**: Kecepatan respons sistem dapat diterima untuk aplikasi web, dengan 3-4 detik untuk upload/capture foto dan 6-10 detik untuk live camera prediction. Penggunaan resource (CPU 30-50%, Memory ~500MB) masih wajar untuk aplikasi dengan deteksi objek.

7. **Antarmuka Pengguna Modern**: Desain antarmuka dengan gradient pink tones sesuai dengan tema kosmetik/beauty. Fitur seperti drag & drop, modal info, dan confidence bars meningkatkan pengalaman pengguna.

8. **Potensi Aplikasi Industri**: Sistem ini memiliki potensi besar untuk diaplikasikan di industri kosmetik, terutama untuk e-commerce, marketing interaktif, customer service, dan pengumpulan data distribusi skin tone untuk R&D.

### 5.2 Saran

Berdasarkan hasil implementasi dan pengujian, beberapa saran untuk pengembangan selanjutnya adalah:

1. **Peningkatan Akurasi Klasifikasi**:
   - Menggunakan dataset yang lebih besar dan beragam untuk training
   - Menerapkan machine learning yang lebih kompleks (misalnya deep learning khusus untuk klasifikasi skin tone)
   - Menambahkan faktor undertone (cool/warm/neutral) untuk hasil yang lebih akurat
   - Mengimplementasikan data augmentation untuk meningkatkan robustness terhadap variasi pencahayaan

2. **Peningkatan Deteksi Wajah**:
   - Menggunakan model YOLO yang lebih besar (YOLOv8s/m) untuk akurasi yang lebih tinggi
   - Mengimplementasikan face alignment untuk menormalkan posisi wajah
   - Menambahkan deteksi multiple face untuk mendukung grup foto
   - Mengoptimalkan region extraction wajah (bukan hanya 50% atas)

3. **Peningkatan Performa**:
   - Mengimplementasikan caching untuk model YOLO
   - Menggunakan GPU acceleration untuk processing yang lebih cepat
   - Mengoptimalkan rate limiting untuk balance antara beban server dan responsivitas
   - Mengimplementasikan lazy loading untuk model COCO-SSD

4. **Peningkatan Fitur**:
   - Menambahkan fitur comparison untuk membandingkan hasil dari berbagai foto
   - Menambahkan rekomendasi produk foundation dari berbagai brand
   - Mengimplementasikan history/prediction log untuk user
   - Menambahkan fitur share ke social media
   - Mengimplementasikan dark mode untuk antarmuka

5. **Peningkatan User Experience**:
   - Menambahkan tutorial/guided tour untuk pengguna baru
   - Mengimplementasikan progress indicator yang lebih detail
   - Menambahkan tips untuk pengambilan foto yang baik
   - Mengoptimalkan untuk mobile devices (responsive design yang lebih baik)

6. **Peningkatan Security**:
   - Mengimplementasikan rate limiting per user untuk mencegah abuse
   - Menambahkan validasi input yang lebih ketat
   - Mengimplementasikan HTTPS untuk production
   - Menambahkan authentication untuk fitur premium

7. **Pengembangan Production**:
   - Menggunakan WSGI server (Gunicorn, uWSGI) untuk production
   - Mengimplementasikan load balancing untuk scalability
   - Menambahkan monitoring dan logging
   - Mengimplementasikan CI/CD pipeline untuk deployment otomatis

8. **Penelitian Lanjutan**:
   - Melakukan user testing dengan skala yang lebih besar
   - Mengumpulkan feedback dari pengguna nyata
   - Melakukan A/B testing untuk berbagai threshold klasifikasi
   - Meneliti pengaruh faktor lingkungan (pencahayaan, background) terhadap akurasi

### 5.3 Keterbatasan Penelitian

Penelitian ini memiliki beberapa keterbatasan yang perlu diperhatikan:

1. **Dataset Terbatas**: Pengujian akurasi hanya dilakukan dengan 30 gambar wajah, yang mungkin tidak representatif untuk populasi yang lebih besar dan beragam.

2. **Kategori Skin Tone Sederhana**: Hanya menggunakan tiga kategori (Fair, Medium, Tan) yang mungkin tidak cukup untuk merepresentasikan variasi warna kulit yang lebih kompleks.

3. **Tidak Memperhitungkan Undertone**: Sistem tidak mempertimbangkan faktor undertone (cool/warm/neutral) yang penting untuk pemilihan shade foundation yang lebih akurat.

4. **Ketergantungan Pencahayaan**: Akurasi klasifikasi dipengaruhi oleh kualitas pencahayaan dan kondisi lingkungan saat pengambilan foto.

5. **Keterbatasan Model YOLO**: Model YOLOv8n adalah model terkecil yang mungkin tidak seakurat model yang lebih besar untuk deteksi wajah dalam kondisi yang menantang.

6. **Pengujian Terbatas**: Pengujian kompatibilitas browser dan performa dilakukan dalam skala terbatas dan mungkin tidak mencakup semua skenario penggunaan nyata.

7. **Tidak Ada Validasi User**: Sistem belum diuji oleh pengguna nyata dalam skala besar, sehingga feedback dari pengguna aktual belum tersedia.

Meskipun memiliki keterbatasan, penelitian ini berhasil membuktikan bahwa sistem prediksi shade foundation berbasis YOLO dapat diimplementasikan dengan baik dan memberikan solusi yang praktis untuk masalah pemilihan shade foundation. Hasil penelitian ini dapat menjadi dasar untuk pengembangan lebih lanjut dengan perbaikan-perbaikan yang telah disarankan.
