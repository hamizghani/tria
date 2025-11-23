from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from .models import Sanggar # Import model

def index(request):
    # Ambil semua data dari database
    sanggars = Sanggar.objects.all()
    context = {
        'sanggars': sanggars
    }
    return render(request, 'daftarsanggar/index.html', context)

def detail(request, sanggar_id):
    # Cari di database, kalau gak ada return 404
    sanggar = get_object_or_404(Sanggar, sanggar_id=sanggar_id)
    
    # wa_link sudah ada di model sebagai property, jadi tidak perlu logic di sini
    
    context = {
        'sanggar': sanggar,
        # Kita tidak perlu pass 'wa_link' terpisah karena bisa diakses via sanggar.wa_link di template
    }
    return render(request, 'daftarsanggar/detail.html', context)
