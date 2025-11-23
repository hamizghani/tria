TRIA - Tari Nusantara AI

📖 Deskripsi Projek
TRIA (Tari Nusantara AI) adalah aplikasi berbasis Artificial Intelligence dan Computer Vision yang berfungsi sebagai media pembelajaran interaktif sekaligus konservasi digital seni tari tradisional Indonesia. Aplikasi ini memanfaatkan teknologi pose estimation dan motion tracking untuk menganalisis gerakan tubuh pengguna secara real-time serta memberikan umpan balik terhadap ketepatan, ritme, dan ekspresi gerak dibandingkan dengan data maestro tari.
🎯 Tujuan Utama

Konservasi Digital - Mendokumentasikan gerakan tarian tradisional Indonesia dalam format data digital terstruktur
Pembelajaran Interaktif - Menyediakan akses belajar tari tradisional berkualitas yang terjangkau dan mudah diakses
Pemberdayaan Ekonomi - Menciptakan kanal digital bagi pelaku budaya untuk memonetisasi keahlian mereka


✨ Fitur Utama
1. 🎭 Daftar Tarian

Katalog lengkap tarian tradisional Indonesia dari berbagai daerah
Informasi detail tentang sejarah, filosofi, dan makna setiap tarian
Metadata budaya yang komprehensif
Filter berdasarkan daerah asal, tingkat kesulitan, dan kategori

2. 🤖 AI Motion Tracking

Deteksi pose real-time menggunakan MediaPipe/OpenPose
Analisis gerakan berbasis 30+ keypoints tubuh
Perbandingan gerakan dengan data maestro
Feedback instan terhadap akurasi gerakan

3. 📊 Model Movement

Database gerakan tari yang terstandarisasi
Pose vectors dan spatial-temporal data
Sistem scoring berbasis AI
Arsip gerak nasional yang terstruktur

4. 🏛️ Daftar Sanggar

Direktori sanggar tari di seluruh Indonesia
Profil lengkap termasuk lokasi, kontak, dan spesialisasi
Integrasi dengan sistem pembelajaran
Review dan rating dari pengguna

5. ℹ️ About & Informasi

Tentang proyek TRIA dan visi misi
Tim pengembang dan kontributor
Dokumentasi teknologi yang digunakan
Panduan penggunaan aplikasi


🛠️ Teknologi yang Digunakan
Backend

Django 4.x - Web framework Python
Django REST Framework - API development
PostgreSQL - Database relasional
Celery - Task queue untuk processing video
Redis - Caching dan message broker

AI/ML Stack

MediaPipe - Pose estimation
OpenPose (PyTorch) - Motion tracking
TensorFlow - AI scoring engine
OpenCV - Video processing
NumPy - Numerical computing
scikit-learn - Machine learning utilities

Frontend (Terpisah)

Django - framework untuk web
Tailwind CSS - Styling

Infrastructure

Docker - Containerization
AWS/Google Cloud - Cloud hosting
GitHub Actions - CI/CD


📦 Instalasi
Prerequisites

Python 3.9+
PostgreSQL 13+
Redis 6+
virtualenv atau conda

Setup Lokal

Clone Repository

bashgit clone https://github.com/yourusername/tria-backend.git
cd tria-backend

Buat Virtual Environment

bashpython -m venv venv
source venv/bin/activate  # Linux/Mac
# atau
venv\Scripts\activate  # Windows

Install Dependencies

bashpip install -r requirements.txt

Setup Environment Variables

bashcp .env.example .env
# Edit .env dengan konfigurasi database dan API keys

Setup Database

bashpython manage.py migrate
python manage.py createsuperuser

Load Initial Data

bashpython manage.py loaddata fixtures/tarian.json
python manage.py loaddata fixtures/sanggar.json

Jalankan Development Server

bashpython manage.py runserver


🧪 Testing
bash# Run semua tests
python manage.py test

# Test specific app
python manage.py test apps.tarian

# Run dengan coverage
coverage run --source='.' manage.py test
coverage report

🚀 Deployment
Docker Deployment
bash# Build image
docker build -t tria-backend .

👥 Tim Pengembang
Tim Little Vietnam

Muhammad Hamiz Ghani Ayusha
Lessyarta Kamali Sopamena Pirade
Ammar Muhammad Rafif
I Gusti Ngurah Agung Airlangga Putra
Fidel Akilah

Pembimbing: Prof. Siti Aminah (Universitas Indonesia)

📄 Lisensi
Project ini dikembangkan untuk BUDAYAGO 2025 dengan kategori Pelestarian dan Konservasi Budaya.
© 2025 Tim Little Vietnam - Universitas Indonesia



🙏 Acknowledgments

Kementerian Pendidikan, Kebudayaan, Riset, dan Teknologi
Universitas Indonesia
Komunitas sanggar tari nusantara
MediaPipe & OpenPose communities
Semua kontributor dan pendukung proyek TRIA


Made with ❤️ for Indonesian Traditional Dance Preservation