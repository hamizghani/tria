from django.shortcuts import render
from django.http import Http404

# Updated list of 10 Indonesian dances with images and youtube placeholders
DANCES = [
    {
        "id": 1,
        "name": "Tari Kecak",
        "description": "Tari Kecak adalah tari tradisional Bali yang berpusat pada paduan suara pria yang mengeluarkan suara 'cak'.",
        "gerakan": ["Gerakan 1", "Gerakan 2", "Gerakan 3", "Gerakan 4"],
        "youtube_id": "sGX_XGdE7eo",  # YouTube video ID only
        "image_url": "https://momopururu.com/wp-content/uploads/2022/06/20211218171844_IMG_8553-01-01-scaled-1024x768.jpeg"
    },
    {
        "id": 2,
        "name": "Tari Janger",
        "description": "Tari Janger adalah tari tradisional dari Bali yang menampilkan gerakan dinamis dan ceria.",
        "gerakan": ["Gerakan 1", "Gerakan 2", "Gerakan 3", "Gerakan 4"],
        "youtube_id": "3ka7bd-ECsI",
        "image_url": "https://img.antarafoto.com/cache/1200x800/2021/07/01/pagelaran-tari-janger-muda-mudi-bali-uq4u-dom.webp"
    },
    {
        "id": 3,
        "name": "Tari Bungong Jeumpa",
        "description": "Tari Bungong Jeumpa adalah tari tradisional Aceh yang melambangkan keindahan bunga Jeumpa.",
        "gerakan": ["Gerakan 1", "Gerakan 2", "Gerakan 3", "Gerakan 4"],
        "youtube_id": "W3PRdCxocM0",
        "image_url": "https://www.kelaspintar.id/_next/image?url=https%3A%2F%2Fblog2.kelaspintar.id%2Fblog%2Fwp-content%2Fuploads%2F2021%2F12%2Ftari-bungong-jeumpa.jpg&w=3840&q=75"
    },
    {
        "id": 4,
        "name": "Tari Lenggang Nyai",
        "description": "Tari Lenggang Nyai adalah tari dari Betawi yang menggambarkan gerakan wanita dengan anggun.",
        "gerakan": ["Berdiri tegap, kaki dibuka selebar bahu, tangan kanan memegang ujung selendang di pinggang kanan, tangan kiri di pinggang kiri. Hitungan 1–8: ayunkan pinggul dan badan sedikit miring ke kanan-kiri secara lembut (lenggang), sambil kaki kanan melangkah kecil ke samping kanan lalu rapat lagi, kaki kiri menyusul ke samping kiri lalu rapat lagi. Ulangi 2 kali (16 hitungan) dengan senyum dan kepala sedikit mengangguk mengikuti arah lenggangan.",

"Mulai dari posisi menghadap depan. Hitungan 1–4: kaki kanan melangkah ke depan sedikit serong kanan, tangan kanan mengangkat selendang setinggi dada, tangan kiri membuka ke samping kiri sejajar bahu. Hitungan 5–8: putar badan pelan ke kiri (setengah lingkaran), kaki kiri menyusul rapat, selendang dikibas lembut ke arah luar. Ulangi pola yang sama ke arah berlawanan: langkah kaki kiri serong depan kiri, tangan kiri angkat selendang, putar badan ke kanan, selendang dikibas lagi (total 16 hitungan).",

"Dari posisi menghadap depan, lakukan langkah silang. Hitungan 1–4: kaki kanan menyilang di depan kaki kiri, lalu kaki kiri melangkah membuka ke samping kiri, tubuh sedikit condong mengikuti arah kaki. Tangan berayun silang di depan badan (seperti mengiris lembut udara) sambil memegang selendang. Hitungan 5–8: ganti, kaki kiri menyilang di depan kaki kanan lalu membuka ke samping kanan, tangan berayun kembali dengan pola yang sama. Ulangi 2 kali (16 hitungan) sambil jaga gerakan tetap halus dan lentur.",

"Gerakan penutup: dari posisi terakhir, rapikan langkah hingga kedua kaki rapat menghadap penonton. Hitungan 1–4: kedua tangan membawa selendang ke depan dada, siku sedikit menekuk, kepala menunduk pelan sebagai salam. Hitungan 5–8: buka tangan ke samping dengan selendang terbentang lembut, dada dibuka, pandangan ke depan sambil tersenyum. Ulangi salam satu kali lagi jika perlu, lalu tahan pose akhir beberapa detik sebelum benar-benar selesai."],
        "youtube_id": "U1ycqGXJ1fI",
        "image_url": "https://www.senibudayabetawi.com/wp-content/uploads/2021/12/large-maxresdefault-1-4d2a0786063540dff664d84bfe0d9d07-2.jpg"
    },
    {
        "id": 5,
        "name": "Tari Piring",
        "description": "Tari Piring adalah tarian tradisional Minangkabau yang menggunakan piring sebagai properti.",
        "gerakan": ["Gerakan 1", "Gerakan 2", "Gerakan 3", "Gerakan 4"],
        "youtube_id": "",
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQe3dCdunJCq8gLwWCdbiWBeqI1VVKZYxH8aw&s"
    },
    {
        "id": 6,
        "name": "Tari Serimpi",
        "description": "Tari Serimpi adalah tari klasik Yogyakarta yang penuh dengan gerakan lemah gemulai.",
        "gerakan": ["Gerakan 1", "Gerakan 2", "Gerakan 3", "Gerakan 4"],
        "youtube_id": "",
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRn-HmkUeHFdSytX9MQ4YMQ8Ggtee8TKTlQFg&s"
    },
    {
        "id": 7,
        "name": "Tari Saman",
        "description": "Tari Saman dari Aceh terkenal dengan gerakan cepat dan kompak.",
        "gerakan": ["Gerakan 1", "Gerakan 2", "Gerakan 3", "Gerakan 4"],
        "youtube_id": "",
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTOqlApZqamkNQq2qamDw9xfm28YlT8cmSXZA&s"
    },
    {
        "id": 8,
        "name": "Tari Reog Ponorogo",
        "description": "Tari Reog Ponorogo adalah pertunjukan tari dengan topeng besar dari Jawa Timur.",
        "gerakan": ["Gerakan 1", "Gerakan 2", "Gerakan 3", "Gerakan 4"],
        "youtube_id": "",
        "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSl7aU7RshzmXtYoXIhgmlyVEZ639AoaB8-CA&s"
    },
    {
        "id": 9,
        "name": "Tari Topeng Betawi",
        "description": "Tari Topeng Betawi menampilkan gerakan yang ceria dengan topeng khas Betawi.",
        "gerakan": ["Gerakan 1", "Gerakan 2", "Gerakan 3", "Gerakan 4"],
        "youtube_id": "",
        "image_url": "https://bisniswisata.co.id/wp-content/uploads/2019/08/tari-topeng-betawi-1.jpg"
    },
    {
        "id": 10,
        "name": "Tari Gambyong",
        "description": "Tari Gambyong adalah tari klasik dari Jawa Tengah dengan gerakan anggun.",
        "gerakan": ["Gerakan 1", "Gerakan 2", "Gerakan 3", "Gerakan 4"],
        "youtube_id": "",
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/1/15/Gambyong_Langenkusuma_Pj_DSC_1322.JPG"
    }
]

def dance_list(request):
    return render(request, 'dances/dance_list.html', {'dances': DANCES})

def get_dance_by_id(dance_id):
    for dance in DANCES:
        if dance["id"] == int(dance_id):
            return dance
    return None

def dance_detail(request, dance_id):
    dance = get_dance_by_id(dance_id)
    if dance is None:
        raise Http404(f"Dance with id {dance_id} not found")
    return render(request, 'dances/dance_detail.html', {'dance': dance})

def dance_tutorial(request, dance_id):
    dance = get_dance_by_id(dance_id)
    if dance is None:
        raise Http404(f"Dance with id {dance_id} not found")
    return render(request, 'dances/dance_tutorial.html', {'dance': dance})

def dance_assessment(request, dance_id):
    dance = get_dance_by_id(dance_id)
    if dance is None:
        raise Http404(f"Dance with id {dance_id} not found")
    return render(request, 'dances/dance_assessment.html', {'dance': dance})

def dance_result(request, dance_id):
    dance = get_dance_by_id(dance_id)
    if dance is None:
        raise Http404(f"Dance with id {dance_id} not found")
    score = 85
    improvement = "Menurutku, waktu kamu bawain Tari Lenggang Nyai, masalah yang paling sering kelihatan itu di keluwesan badan dan ekspresi wajah; gerak kaki dan pola lantainya sudah lumayan hafal, tapi ayunan tangan, bahu, dan pinggulmu masih cenderung kaku sehingga kesan lincah dan centil khas tari ini belum terlalu terasa, ditambah kadang tempo kamu suka sedikit kecepatan lalu tiba-tiba melambat sehingga nggak selalu “nempel” dengan iringan musik, jadi ke depan kamu bisa lebih fokus melenturkan badan, menguatkan mimik (senyum, tatapan mata yang hidup), dan sering latihan pakai musik supaya rasa dan ritmenya lebih rata dari awal sampai akhir."
    return render(request, 'dances/dance_result.html', {
        'dance': dance,
        'score': score,
        'improvement': improvement
    })
