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
        "youtube_id": "",
        "image_url": ""
    },
    {
        "id": 3,
        "name": "Tari Bungong Jeumpa",
        "description": "Tari Bungong Jeumpa adalah tari tradisional Aceh yang melambangkan keindahan bunga Jeumpa.",
        "gerakan": ["Gerakan 1", "Gerakan 2", "Gerakan 3", "Gerakan 4"],
        "youtube_id": "",
        "image_url": ""
    },
    {
        "id": 4,
        "name": "Tari Lenggang Nyai",
        "description": "Tari Lenggang Nyai adalah tari dari Betawi yang menggambarkan gerakan wanita dengan anggun.",
        "gerakan": ["Gerakan 1", "Gerakan 2", "Gerakan 3", "Gerakan 4"],
        "youtube_id": "",
        "image_url": ""
    },
    {
        "id": 5,
        "name": "Tari Piring",
        "description": "Tari Piring adalah tarian tradisional Minangkabau yang menggunakan piring sebagai properti.",
        "gerakan": ["Gerakan 1", "Gerakan 2", "Gerakan 3", "Gerakan 4"],
        "youtube_id": "",
        "image_url": ""
    },
    {
        "id": 6,
        "name": "Tari Serimpi",
        "description": "Tari Serimpi adalah tari klasik Yogyakarta yang penuh dengan gerakan lemah gemulai.",
        "gerakan": ["Gerakan 1", "Gerakan 2", "Gerakan 3", "Gerakan 4"],
        "youtube_id": "",
        "image_url": ""
    },
    {
        "id": 7,
        "name": "Tari Saman",
        "description": "Tari Saman dari Aceh terkenal dengan gerakan cepat dan kompak.",
        "gerakan": ["Gerakan 1", "Gerakan 2", "Gerakan 3", "Gerakan 4"],
        "youtube_id": "",
        "image_url": ""
    },
    {
        "id": 8,
        "name": "Tari Reog Ponorogo",
        "description": "Tari Reog Ponorogo adalah pertunjukan tari dengan topeng besar dari Jawa Timur.",
        "gerakan": ["Gerakan 1", "Gerakan 2", "Gerakan 3", "Gerakan 4"],
        "youtube_id": "",
        "image_url": ""
    },
    {
        "id": 9,
        "name": "Tari Topeng Betawi",
        "description": "Tari Topeng Betawi menampilkan gerakan yang ceria dengan topeng khas Betawi.",
        "gerakan": ["Gerakan 1", "Gerakan 2", "Gerakan 3", "Gerakan 4"],
        "youtube_id": "",
        "image_url": ""
    },
    {
        "id": 10,
        "name": "Tari Gambyong",
        "description": "Tari Gambyong adalah tari klasik dari Jawa Tengah dengan gerakan anggun.",
        "gerakan": ["Gerakan 1", "Gerakan 2", "Gerakan 3", "Gerakan 4"],
        "youtube_id": "",
        "image_url": ""
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
