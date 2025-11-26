TRIA

📖 Deskripsi Projek
TRIA adalah aplikasi berbasis Artificial Intelligence dan Computer Vision yang berfungsi sebagai media pembelajaran interaktif sekaligus konservasi digital seni tari tradisional Indonesia. Aplikasi ini memanfaatkan teknologi pose estimation dan motion tracking untuk menganalisis gerakan tubuh pengguna secara real-time serta memberikan umpan balik terhadap ketepatan, ritme, dan ekspresi gerak dibandingkan dengan data maestro tari.

🎯 Tujuan Utama
Konservasi Digital - Mendokumentasikan gerakan tarian tradisional Indonesia dalam format data digital terstruktur
Pembelajaran Interaktif - Menyediakan akses belajar tari tradisional berkualitas yang terjangkau dan mudah diakses
Pemberdayaan Ekonomi - Menciptakan kanal digital bagi pelaku budaya untuk memonetisasi keahlian mereka

Fitur utama
- Katalog tarian tradisional lengkap dengan detail dan tutorial
- Penilaian berbasis kamera menggunakan pose estimation dan scoring otomatis
- Direktori sanggar dengan informasi kontak dan lokasi
- Akun pengguna (registrasi/login/profil) dan manajemen sesi
- Halaman hasil dan progres dengan umpan balik sub-gerakan

Stack Teknologi

- Backend: Python + Django (proyek ini menggunakan Django 5.x)
- Database: SQLite untuk pengembangan lokal; PostgreSQL direkomendasikan untuk produksi
- Frontend: Template Django, JavaScript vanilla, CSS (menggunakan variabel CSS dan gaya mirip Tailwind pada beberapa bagian)
- AI / CV: Integrasi MediaPipe / OpenPose untuk pose estimation, OpenCV untuk pemrosesan video, TensorFlow / PyTorch untuk model penilaian
- Antrian tugas (opsional): Celery + Redis untuk pemrosesan background (mis. video atau tugas model)
- Deployment: WSGI (gunicorn), Docker (opsional), berkas statis via `collectstatic` / WhiteNoise atau web server (nginx)

Panduan singkat — Pengembangan lokal

1. Buat dan aktifkan virtual environment

```powershell
python -m venv env
env\Scripts\Activate.ps1    # PowerShell pada Windows
```

2. Pasang dependensi

```powershell
pip install -r requirements.txt
```

3. Terapkan migrasi dan buat superuser

```powershell
python manage.py migrate
python manage.py createsuperuser
```

4. Jalankan server pengembangan

```powershell
python manage.py runserver
```

Buka http://127.0.0.1:8000 di peramban Anda.

Catatan deployment
- Tetapkan `PRODUCTION=true` (atau pastikan `DEBUG=False`) dan atur `ALLOWED_HOSTS` serta `CSRF_TRUSTED_ORIGINS` ke domain Anda (sertakan scheme, mis. `https://contoh.com`).
- Jalankan `python manage.py collectstatic --noinput` dan layani folder `staticfiles/` melalui web server (nginx) atau gunakan WhiteNoise untuk deployment sederhana.
- Jika TLS diakhiri oleh load balancer / reverse proxy, pastikan header `X-Forwarded-Proto: https` diteruskan dan sesuaikan `SECURE_PROXY_SSL_HEADER` di pengaturan Django.

Struktur repositori (secara ringkas)
- `tria/` — pengaturan proyek dan titik masuk (settings.py, urls.py)
- `dances/` — katalog tarian, tampilan assessment dan tutorial
- `daftarsanggar/` — direktori sanggar dan halaman detail
- `authentication/` — login, register, profil dan template terkait
- `main/`, `articles/` dan aplikasi pendukung lainnya

Contributor TEAM (Little Vietnam)