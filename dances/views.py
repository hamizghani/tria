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
        "gerakan": ["Gerakan 1", "Gerakan 2", "Gerakan 3", "Gerakan 4"],
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
    improvement = "Perbaiki gerakan tangan dan postur."
    return render(request, 'dances/dance_result.html', {
        'dance': dance,
        'score': score,
        'improvement': improvement
    })
