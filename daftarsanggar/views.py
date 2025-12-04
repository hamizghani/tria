from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Sanggar # Import model
import re


# Hardcoded sanggar data instead of relying on import_data.py
HARDCODED_SANGGARS = [
    {
        "sanggar_id": "ST001",
        "nama_sanggar": "Namarina Dance Academy",
        "image": "https://cdn.antaranews.com/cache/360x240/2021/12/05/65-Tahun-Namarina-Berkarya-051221-MRH-10.jpg",
        "phone_number": "(021) 8294777",
        "location": "Jl. Halimun No. 43, Guntur, Jakarta Selatan",
        "email": "info.namarina@gmail.com",
        "description": "Institusi pendidikan tari tertua di Indonesia (sejak 1956) yang fokus pada Ballet, Jazz Dance, dan kebugaran.",
        "wa_link": "https://api.whatsapp.com/send/?phone=62810&text&type=phone_number&app_absent=0",
        "reviews": [
            {"user": "Andi Pratama", "comment": "Pengajar sangat profesional."}
        ]
    },
    {
        "sanggar_id": "ST002",
        "nama_sanggar": "Gigi Art of Dance",
        #"image": "daftarsanggar/img/gigiartofdance.png",
        "image": "https://cdn.grid.id/crop/0x0:0x0/700x465/photo/2023/12/21/_mg_9565jpg-20231221111126.jpg",
        "phone_number": "(021) 7399739",
        "location": "Jl. Radio Dalam Raya No. 191, Jakarta Selatan",
        "email": "info@gigiartofdance.id",
        "description": "Sanggar tari modern yang dinamis, terkenal dengan kelas Broadway, Hip Hop, dan Contemporary.",
        "wa_link": "https://api.whatsapp.com/send/?phone=62810&text&type=phone_number&app_absent=0",
        "reviews": [
            {"user": "Fajar Nugraha", "comment": "Koreografinya keren banget!"}
        ]
    },
    {
        "sanggar_id": "ST003",
        "nama_sanggar": "Sanggar Ayodya Pala",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQOAQwcejFLv6NLsW9lwGipvLIONrzYP7MRFg&s",
        "phone_number": "(021) 7775678",
        "location": "Jl. Melati Raya No. 5, Depok Jaya, Kota Depok",
        "email": "ayodyapala@yahoo.com",
        "description": "Pusat kesenian yang sangat aktif melestarikan tari tradisional Jawa, Sunda, dan Bali di wilayah Depok.",
        "wa_link": "https://api.whatsapp.com/send/?phone=62810&text&type=phone_number&app_absent=0",
        "reviews": [
            {"user": "Agus Salim", "comment": "Tempat terbaik belajar tari tradisi."}
        ]
    },
    {
        "sanggar_id": "ST004",
        "nama_sanggar": "Marlupi Dance Academy",
        "image": "https://awsimages.detik.net.id/community/media/visual/2022/04/24/marlupi-dance-academy_43.jpeg?w=1200",
        "phone_number": "(021) 5656303",
        "location": "Green Ville Maisonette Blok FA No. 15, Jakarta Barat",
        "email": "admin@marlupi.com",
        "description": "Akademi tari berstandar internasional (Royal Academy of Dance) yang mencetak banyak balerina profesional.",
        "wa_link": "https://api.whatsapp.com/send/?phone=62810&text&type=phone_number&app_absent=0",
        "reviews": [
            {"user": "Citra Kirana", "comment": "Standar internasionalnya terasa."}
        ]
    },
    {
        "sanggar_id": "ST005",
        "nama_sanggar": "United Dance Works",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT2xjqcNb8zXIsEuRB9okyeFpZRP__XwCx2lQ&s",
        "phone_number": "+62 877-8017-7202",
        "location": "Jl. Bangka XI No. 3A-1, Kemang, Jakarta Selatan",
        "email": "info@uniteddanceworks.com",
        "description": "Basecamp bagi penari profesional dengan spesialisasi Showbiz, Hip Hop, dan tari komersial.",
        "wa_link": "https://api.whatsapp.com/send/?phone=62810&text&type=phone_number&app_absent=0",
        "reviews": [
            {"user": "Indra Bekti", "comment": "Keren untuk yang suka kontemporer."}
        ]
    },
    {
        "sanggar_id": "ST006",
        "nama_sanggar": "Sanggar Puspo Budoyo",
        "image": "https://www.puspobudoyo.com/wp-content/uploads/2025/01/hero-2.webp",
        "phone_number": "(021) 74713555",
        "location": "Jl. Elang Raya No.1, Ciputat, Tangerang Selatan",
        "email": "contact@puspobudoyo.com",
        "description": "Kampung seni budaya yang komprehensif, mengajarkan tari, musik gamelan, dan teater ketoprak.",
        "wa_link": "https://api.whatsapp.com/send/?phone=62810&text&type=phone_number&app_absent=0",
        "reviews": [
            {"user": "Nadine", "comment": "Suasana kampung seninya asri."}
        ]
    },
    {
        "sanggar_id": "ST007",
        "nama_sanggar": "EKI Dance Company",
        "image": "https://indonesiakaya.com/wp-content/uploads/2020/11/eki-dance-company-pentaskan-eki-update-41-broadwaynyaindonesia.jpg",
        "phone_number": "(021) 8312377",
        "location": "Jl. Padang No. 21, Manggarai, Jakarta Selatan",
        "email": "eki@ekidancecompany.com",
        "description": "Perusahaan tari profesional ternama yang memproduksi pertunjukan musikal dan tari kontemporer.",
        "wa_link": "https://api.whatsapp.com/send/?phone=62810&text&type=phone_number&app_absent=0",
        "reviews": [
            {"user": "Sule", "comment": "Karya-karyanya selalu out of the box."}
        ]
    },
    {
        "sanggar_id": "ST008",
        "nama_sanggar": "Sanggar Cipta Budaya",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSij7DGPL0-nJRoBEIahDfkpntJ1qB2TDcnig&s",
        "phone_number": "0878-8077-6402",
        "location": "Jl. Taman Asri Lama No. 16, Tangerang",
        "email": "ciptaartdance@gmail.com",
        "description": "Menyediakan jasa pertunjukan tari adat Nusantara, kostum tari, dan pelatihan tari privat.",
        "wa_link": "https://api.whatsapp.com/send/?phone=62810&text&type=phone_number&app_absent=0",
        "reviews": [
            {"user": "Yuni Shara", "comment": "Tari Jaipongnya luwes."}
        ]
    },
    {
        "sanggar_id": "ST009",
        "nama_sanggar": "Forever Dance Center",
        "image": "https://i.ytimg.com/vi/pByOSHAVglI/maxresdefault.jpg",
        "phone_number": "0812-9642-0360",
        "location": "Jl. Pulomas Timur 2, Jakarta Timur",
        "email": "ForeverDanceCenter@gmail.com",
        "description": "Sekolah tari populer untuk anak-anak hingga dewasa dengan genre Ballet, K-Pop, dan Hip Hop.",
        "wa_link": "https://api.whatsapp.com/send/?phone=62810&text&type=phone_number&app_absent=0",
        "reviews": [
            {"user": "Cinta Laura", "comment": "Dance cover K-Pop nya update."}
        ]
    },
    {
        "sanggar_id": "ST010",
        "nama_sanggar": "Kinarya GSP",
        "image": "https://www.whiteboardjournal.com/wp-content/themes/whiteboardjournal/media.php?src=https://www.whiteboardjournal.com/wp-content/uploads/2018/12/DSCF3490-748x499.jpg&w=750&h=500&zc=1&q=90",
        "phone_number": "0858-8419-3546",
        "location": "Jl. Wijaya I No. 381A, Jaksel",
        "email": "info@kinarya.id",
        "description": "Sanggar milik Guruh Soekarno Putra yang fokus pada tari kreasi baru bernuansa Indonesia.",
        "wa_link": "https://api.whatsapp.com/send/?phone=62810&text&type=phone_number&app_absent=0",
        "reviews": [
            {"user": "Hanggini", "comment": "Tari kreasi barunya unik."}
        ]
    },
    {
        "sanggar_id": "ST011",
        "nama_sanggar": "Steps Dance Academy",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTc5qqI9gIpZ_ZJ34VHZAMIUK9GRefUU1JfWQ&s",
        "phone_number": "(021) 25554454",
        "location": "fX Sudirman 7th Floor, Jakarta Pusat",
        "email": "stepsdancefx@gmail.com",
        "description": "Studio tari modern di pusat kota yang menawarkan berbagai genre dari Jazz hingga Urban Dance.",
        "wa_link": "https://api.whatsapp.com/send/?phone=62810&text&type=phone_number&app_absent=0",
        "reviews": [
            {"user": "Raisa", "comment": "Lokasi strategis di mall."}
        ]
    },
    {
        "sanggar_id": "ST012",
        "nama_sanggar": "Sanggar Betawi Setu Babakan",
        "image": "https://cdn.antaranews.com/cache/1200x800/2025/07/16/IMG-20250714-WA0015.jpg",
        "phone_number": "(021) 78893258",
        "location": "Perkampungan Budaya Betawi Setu Babakan",
        "email": "betawi@setubabakan.or.id",
        "description": "Pusat pelatihan seni budaya Betawi asli (Lenong, Tari Topeng, Gambang Kromong).",
        "wa_link": "https://api.whatsapp.com/send/?phone=62810&text&type=phone_number&app_absent=0",
        "reviews": [
            {"user": "Reza Rahadian", "comment": "Melestarikan budaya Betawi asli."}
        ]
    },
    {
        "sanggar_id": "ST013",
        "nama_sanggar": "Ballet Sumber Cipta",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQqpuJP-yezqT3tgIRzA_--pDVl4YDKKsxVQQ&s",
        "phone_number": "(021) 7659876",
        "location": "Jl. Ciputat Raya No. 1, Pondok Pinang",
        "email": "info@ballet.id",
        "description": "Sekolah balet legendaris yang menggunakan metode Vaganova.",
        "wa_link": "https://api.whatsapp.com/send/?phone=62810&text&type=phone_number&app_absent=0",
        "reviews": [
            {"user": "Yuki Kato", "comment": "Postur tubuh jadi tegap."}
        ]
    },
    {
        "sanggar_id": "ST014",

        "nama_sanggar": "Sanggar Kinang Putra",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-q5Bm1D-IcpCM642aYf6olNiF_xD3WP_HEg&s",
        "phone_number": "0813-8080-1234",
        "location": "Jl. Putri Tunggal, Cimanggis",
        "email": "kinangputra@yahoo.com",
        "description": "Sanggar bersejarah yang melestarikan Topeng Betawi Cisalak dan Tari Cokek.",
        "wa_link": "https://api.whatsapp.com/send/?phone=62810&text&type=phone_number&app_absent=0",
        "reviews": [
            {"user": "Chelsea Islan", "comment": "Sangat otentik tariannya."}
        ]
    },
    {
        "sanggar_id": "ST015",
        "nama_sanggar": "Gema Citra Nusantara",
        "image": "https://xposeindonesia.com/wp-content/uploads/2021/02/1f9e52f5766a7a5e24af756d4d3b3708_XL.jpg",
        "phone_number": "(021) 725 3573",
        "location": "Jl. Wolter Monginsidi No. 78, Jaksel",
        "email": "info@gcn-indonesia.com",
        "description": "Sanggar tari yang fokus pada promosi budaya Indonesia ke internasional melalui misi budaya.",
        "wa_link": "https://api.whatsapp.com/send/?phone=62810&text&type=phone_number&app_absent=0",
        "reviews": [
            {"user": "Hesti", "comment": "Sering diajak misi budaya."}
        ]
    },
    {
        "sanggar_id": "ST016",
        "nama_sanggar": "Interlude Dance Studio",
        "image": "https://pbs.twimg.com/media/BapUWc-CAAE_usn?format=jpg&name=small",
        "phone_number": "0877-7155-2016",
        "location": "BSD City, Tangerang Selatan",
        "email": "-",
        "description": "Studio tari modern di BSD menawarkan kelas K-Pop Cover, Hip Hop, dan Kids Dance.",
        "wa_link": "https://api.whatsapp.com/send/?phone=62810&text&type=phone_number&app_absent=0",
        "reviews": [
            {"user": "Cak Lontong", "comment": "Anak saya suka kelas K-pop nya."}
        ]
    },
    {
        "sanggar_id": "ST017",
        "nama_sanggar": "Genecela Dance Centre",
        "image": "https://assets.promediateknologi.id/crop/0x0:0x0/750x500/webp/photo/suarakarya/20191028110600IMG_20191028_092326.jpg",
        "phone_number": "(021) 58302528",
        "location": "Jl. Meruya Ilir No. 88, Jakarta Barat",
        "email": "gdc@genecela.com",
        "description": "Pusat pelatihan tari dengan kurikulum internasional untuk Jazz, Tap, dan Ballet.",
        "wa_link": "https://api.whatsapp.com/send/?phone=62810&text&type=phone_number&app_absent=0",
        "reviews": [
            {"user": "Raditya Dika", "comment": "Tap dance jarang ada di tempat lain."}
        ]
    },
    {
        "sanggar_id": "ST018",
        "nama_sanggar": "Sanggar Bintang Asti",
        "image": "https://komunitasondelondeljakarta.com/wp-content/uploads/2019/07/WhatsApp-Image-2019-07-14-at-00.12.12-300x225.jpeg",
        "phone_number": "0857-1600-7521",
        "location": "Pulo Gadung, Jakarta Timur",
        "email": "-",
        "description": "Sanggar seni Betawi yang membina anak muda dengan ondel-ondel dan tari.",
        "wa_link": "https://api.whatsapp.com/send/?phone=62810&text&type=phone_number&app_absent=0",
        "reviews": [
            {"user": "Wika Salim", "comment": "Komunitasnya solid."}
        ]
    },
    {
        "sanggar_id": "ST019",
        "nama_sanggar": "Sanggar Ananda Kawula Muda",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQftYW68CJoXAyHdiKAbr8wqzkWDLQL4rBzig&s",
        "phone_number": "0819-7761-1919",
        "location": "Jl. Dr. Saharjo No. 45, Manggarai",
        "email": "akawulamuda@gmail.com",
        "description": "Sanggar legendaris pimpinan Aditya Gumay, fokus akting dan tari.",
        "wa_link": "https://api.whatsapp.com/send/?phone=62810&text&type=phone_number&app_absent=0",
        "reviews": [
            {"user": "Melly Goeslaw", "comment": "Paket komplit seni peran dan tari."}
        ]
    },
    {
        "sanggar_id": "STO20",
        "nama_sanggar": "Sanggar Ratna Sari",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRAQW7ssArfFoUVgUcUi2QOwaPwh-VPi6qWhA&s",
        "phone_number": "-",
        "location": "Cimanggis, Depok",
        "email": "-",
        "description": "Salah satu sanggar Topeng Betawi tertua kelolaan keluarga H. Bokir.",
        "wa_link": "https://api.whatsapp.com/send/?phone=62810&text&type=phone_number&app_absent=0",
        "reviews": [
            {"user": "Haringga", "comment": "Sangat otentik gaya topengnya."}
        ]
    }
]

@login_required
def index(request):
    context = {
        'sanggars': HARDCODED_SANGGARS
    }
    return render(request, 'daftarsanggar/index.html', context)

@login_required
def detail(request, sanggar_id):
    # Cari sanggar berdasarkan ID
    sanggar_data = next((s for s in HARDCODED_SANGGARS if s["sanggar_id"] == sanggar_id), None)
    
    if not sanggar_data:
        raise Http404("Sanggar not found")
    
    # PENTING: Kita copy object-nya agar tidak mengubah data global asli secara permanen (best practice)
    sanggar = sanggar_data.copy()
    
    # --- LOGIC PERBAIKAN WA ---
    # Ambil nomor telepon dari data
    raw_phone = sanggar.get('phone_number', '')
    
    # Bersihkan nomor menggunakan helper function di atas
    clean_phone = format_whatsapp_number(raw_phone)
    
    if clean_phone:
        # Generate URL WhatsApp yang benar secara dinamis
        # Menggunakan format wa.me yang lebih ringkas atau api.whatsapp.com
        text_msg = "Halo, saya melihat profil sanggar Anda di website dan ingin bertanya info lebih lanjut."
        sanggar['wa_link'] = f"https://api.whatsapp.com/send/?phone={clean_phone}&text={text_msg}"
    else:
        # Jika nomor tidak valid (misal "-"), kosongkan wa_link agar tombol jadi disabled di HTML
        sanggar['wa_link'] = None

    context = {
        'sanggar': sanggar,
    }
    return render(request, 'daftarsanggar/detail.html', context)
    
def format_whatsapp_number(phone_raw):
    # 1. Jika data kosong atau "-", return None
    if not phone_raw or phone_raw == "-":
        return None
    
    # 2. Hapus semua karakter yang BUKAN angka (hapus spasi, -, (), +)
    clean_number = re.sub(r'\D', '', phone_raw)
    
    # 3. Ubah format 0 di depan menjadi 62 (Kode Negara Indonesia)
    if clean_number.startswith('0'):
        clean_number = '62' + clean_number[1:]
    
    # 4. Validasi panjang nomor (nomor HP/Telp Indonesia minimal ~9-10 digit)
    if len(clean_number) < 9:
        return None
        
    return clean_number
