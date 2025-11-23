import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tria.settings')
django.setup()

from daftarsanggar.models import Sanggar, Review

# DATA DENGAN LINK GAMBAR STABIL (Unsplash & Wikimedia)
data_json = [
  {
    "sanggar_id": "ST001",
    "nama_sanggar": "Namarina Dance Academy",
    # Foto Ballet Class
    "image": "namarina.png",
    "phone_number": "(021) 8294777",
    "location": "Jl. Halimun No. 43, Guntur, Jakarta Selatan",
    "email": "info.namarina@gmail.com",
    "description": "Institusi pendidikan tari tertua di Indonesia (sejak 1956) yang fokus pada Ballet, Jazz Dance, dan kebugaran.",
    "reviews": [ { "user": "Andi Pratama", "comment": "Pengajar sangat profesional." } ]
  },
  {
    "sanggar_id": "ST002",
    "nama_sanggar": "Gigi Art of Dance",
    # Foto Modern Dance / Hip Hop
    "image": "gigiartofdance.png",
    "phone_number": "(021) 7399739",
    "location": "Jl. Radio Dalam Raya No. 191, Jakarta Selatan",
    "email": "info@gigiartofdance.id",
    "description": "Sanggar tari modern yang dinamis, terkenal dengan kelas Broadway, Hip Hop, dan Contemporary.",
    "reviews": [ { "user": "Fajar Nugraha", "comment": "Koreografinya keren banget!" } ]
  },
  {
    "sanggar_id": "ST003",
    "nama_sanggar": "Sanggar Ayodya Pala",
    # Foto Tari Tradisional (Vibes Jawa/Bali)
    "image": "ayodyapala.png",
    "phone_number": "(021) 7775678",
    "location": "Jl. Melati Raya No. 5, Depok Jaya, Kota Depok",
    "email": "ayodyapala@yahoo.com",
    "description": "Pusat kesenian yang sangat aktif melestarikan tari tradisional Jawa, Sunda, dan Bali di wilayah Depok.",
    "reviews": [ { "user": "Agus Salim", "comment": "Tempat terbaik belajar tari tradisi." } ]
  },
  {
    "sanggar_id": "ST004",
    "nama_sanggar": "Marlupi Dance Academy",
    # Foto Ballerina Professional
    "image": "marlupi.png",
    "phone_number": "(021) 5656303",
    "location": "Green Ville Maisonette Blok FA No. 15, Jakarta Barat",
    "email": "admin@marlupi.com",
    "description": "Akademi tari berstandar internasional (Royal Academy of Dance) yang mencetak banyak balerina profesional.",
    "reviews": [ { "user": "Citra Kirana", "comment": "Standar internasionalnya terasa." } ]
  },
  {
    "sanggar_id": "ST005",
    "nama_sanggar": "United Dance Works",
    # Foto Urban / Showbiz Dance
    "image": "uniteddance.png",
    "phone_number": "+62 877-8017-7202",
    "location": "Jl. Bangka XI No. 3A-1, Kemang, Jakarta Selatan",
    "email": "info@uniteddanceworks.com",
    "description": "Basecamp bagi penari profesional dengan spesialisasi Showbiz, Hip Hop, dan tari komersial.",
    "reviews": [ { "user": "Indra Bekti", "comment": "Keren untuk yang suka kontemporer." } ]
  },
  {
    "sanggar_id": "ST006",
    "nama_sanggar": "Sanggar Puspo Budoyo",
    # Foto Gamelan / Budaya Jawa
    "image": "puspabudoyo.png",
    "phone_number": "(021) 74713555",
    "location": "Jl. Elang Raya No.1, Ciputat, Tangerang Selatan",
    "email": "contact@puspobudoyo.com",
    "description": "Kampung seni budaya yang komprehensif, mengajarkan tari, musik gamelan, dan teater ketoprak.",
    "reviews": [ { "user": "Nadine", "comment": "Suasana kampung seninya asri." } ]
  },
  {
    "sanggar_id": "ST007",
    "nama_sanggar": "EKI Dance Company",
    # Foto Theatrical / Stage Performance
    "image": "ekidancecompany.png",
    "phone_number": "(021) 8312377",
    "location": "Jl. Padang No. 21, Manggarai, Jakarta Selatan",
    "email": "eki@ekidancecompany.com",
    "description": "Perusahaan tari profesional ternama yang memproduksi pertunjukan musikal dan tari kontemporer.",
    "reviews": [ { "user": "Sule", "comment": "Karya-karyanya selalu out of the box." } ]
  },
  {
    "sanggar_id": "ST008",
    "nama_sanggar": "Sanggar Cipta Budaya",
    # Foto Penari Tradisional dengan Kostum Lengkap
    "image": "ciptabudoyo.png",
    "phone_number": "0878-8077-6402",
    "location": "Jl. Taman Asri Lama No. 16, Tangerang",
    "email": "ciptaartdance@gmail.com",
    "description": "Menyediakan jasa pertunjukan tari adat Nusantara, kostum tari, dan pelatihan tari privat.",
    "reviews": [ { "user": "Yuni Shara", "comment": "Tari Jaipongnya luwes." } ]
  },
  {
    "sanggar_id": "ST009",
    "nama_sanggar": "Forever Dance Center",
    # Foto Studio Dance Modern (K-Pop vibe)
    "image": "https://images.unsplash.com/photo-1524594152303-9fd13543fe6e?q=80&w=800&auto=format&fit=crop",
    "phone_number": "0812-9642-0360",
    "location": "Jl. Pulomas Timur 2, Jakarta Timur",
    "email": "ForeverDanceCenter@gmail.com",
    "description": "Sekolah tari populer untuk anak-anak hingga dewasa dengan genre Ballet, K-Pop, dan Hip Hop.",
    "reviews": [ { "user": "Cinta Laura", "comment": "Dance cover K-Pop nya update." } ]
  },
  {
    "sanggar_id": "ST010",
    "nama_sanggar": "Kinarya GSP",
    # Foto Tari Kreasi Indonesia
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Tari_Saman_from_Aceh.jpg/640px-Tari_Saman_from_Aceh.jpg",
    "phone_number": "0858-8419-3546",
    "location": "Jl. Wijaya I No. 381A, Jaksel",
    "email": "info@kinarya.id",
    "description": "Sanggar milik Guruh Soekarno Putra yang fokus pada tari kreasi baru bernuansa Indonesia.",
    "reviews": [ { "user": "Hanggini", "comment": "Tari kreasi barunya unik." } ]
  },
  {
    "sanggar_id": "ST011",
    "nama_sanggar": "Steps Dance Academy",
    # Foto Latihan Dance di Studio
    "image": "https://images.unsplash.com/photo-1504609773096-104ff2c73ba4?q=80&w=800&auto=format&fit=crop",
    "phone_number": "(021) 25554454",
    "location": "fX Sudirman 7th Floor, Jakarta Pusat",
    "email": "stepsdancefx@gmail.com",
    "description": "Studio tari modern di pusat kota yang menawarkan berbagai genre dari Jazz hingga Urban Dance.",
    "reviews": [ { "user": "Raisa", "comment": "Lokasi strategis di mall." } ]
  },
  {
    "sanggar_id": "ST012",
    "nama_sanggar": "Sanggar Betawi Setu Babakan",
    # Foto Ondel-Ondel (Wikimedia - Stabil)
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Ondel-ondel_at_Jalan_Jaksa_Festival.jpg/640px-Ondel-ondel_at_Jalan_Jaksa_Festival.jpg",
    "phone_number": "(021) 78893258",
    "location": "Perkampungan Budaya Betawi Setu Babakan",
    "email": "betawi@setubabakan.or.id",
    "description": "Pusat pelatihan seni budaya Betawi asli (Lenong, Tari Topeng, Gambang Kromong).",
    "reviews": [ { "user": "Reza Rahadian", "comment": "Melestarikan budaya Betawi asli." } ]
  },
  {
    "sanggar_id": "ST013",
    "nama_sanggar": "Ballet Sumber Cipta",
    # Foto Ballet Pose
    "image": "https://images.unsplash.com/photo-1517559139268-96359eb38c4d?q=80&w=800&auto=format&fit=crop",
    "phone_number": "(021) 7659876",
    "location": "Jl. Ciputat Raya No. 1, Pondok Pinang",
    "email": "info@ballet.id",
    "description": "Sekolah balet legendaris yang menggunakan metode Vaganova.",
    "reviews": [ { "user": "Yuki Kato", "comment": "Postur tubuh jadi tegap." } ]
  },
  {
    "sanggar_id": "ST014",
    "nama_sanggar": "Sanggar Kinang Putra",
    # Foto Topeng (Wikimedia - Stabil)
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/Tari_Topeng.jpg/640px-Tari_Topeng.jpg",
    "phone_number": "0813-8080-1234",
    "location": "Jl. Putri Tunggal, Cimanggis",
    "email": "kinangputra@yahoo.com",
    "description": "Sanggar bersejarah yang melestarikan Topeng Betawi Cisalak dan Tari Cokek.",
    "reviews": [ { "user": "Chelsea Islan", "comment": "Sangat otentik tariannya." } ]
  },
  {
    "sanggar_id": "ST015",
    "nama_sanggar": "Gema Citra Nusantara",
    # Foto Penari Indonesia (Warna Warni)
    "image": "https://images.unsplash.com/photo-1522851888496-e10df23684a0?q=80&w=800&auto=format&fit=crop",
    "phone_number": "(021) 725 3573",
    "location": "Jl. Wolter Monginsidi No. 78, Jaksel",
    "email": "info@gcn-indonesia.com",
    "description": "Sanggar tari yang fokus pada promosi budaya Indonesia ke internasional melalui misi budaya.",
    "reviews": [ { "user": "Hesti", "comment": "Sering diajak misi budaya." } ]
  },
  {
    "sanggar_id": "ST016",
    "nama_sanggar": "Interlude Dance Studio",
    # Foto K-Pop Style Group
    "image": "https://images.unsplash.com/photo-1621976498727-9e5d6d808c4d?q=80&w=800&auto=format&fit=crop",
    "phone_number": "0877-7155-2016",
    "location": "BSD City, Tangerang Selatan",
    "email": "-",
    "description": "Studio tari modern di BSD menawarkan kelas K-Pop Cover, Hip Hop, dan Kids Dance.",
    "reviews": [ { "user": "Cak Lontong", "comment": "Anak saya suka kelas K-pop nya." } ]
  },
  {
    "sanggar_id": "ST017",
    "nama_sanggar": "Genecela Dance Centre",
    # Foto Tap Shoes / Jazz
    "image": "https://images.unsplash.com/photo-1551695405-02117565c589?q=80&w=800&auto=format&fit=crop",
    "phone_number": "(021) 58302528",
    "location": "Jl. Meruya Ilir No. 88, Jakarta Barat",
    "email": "gdc@genecela.com",
    "description": "Pusat pelatihan tari dengan kurikulum internasional untuk Jazz, Tap, dan Ballet.",
    "reviews": [ { "user": "Raditya Dika", "comment": "Tap dance jarang ada di tempat lain." } ]
  },
  {
    "sanggar_id": "ST018",
    "nama_sanggar": "Sanggar Bintang Asti",
    # Foto Anak-anak Menari
    "image": "https://images.unsplash.com/photo-1628108426027-e9a623089d7b?q=80&w=800&auto=format&fit=crop",
    "phone_number": "0857-1600-7521",
    "location": "Pulo Gadung, Jakarta Timur",
    "email": "-",
    "description": "Sanggar seni Betawi yang membina anak muda dengan ondel-ondel dan tari.",
    "reviews": [ { "user": "Wika Salim", "comment": "Komunitasnya solid." } ]
  },
  {
    "sanggar_id": "ST019",
    "nama_sanggar": "Sanggar Ananda Kawula Muda",
    # Foto Acting / Theater
    "image": "https://images.unsplash.com/photo-1518116520779-79883907797e?q=80&w=800&auto=format&fit=crop",
    "phone_number": "0819-7761-1919",
    "location": "Jl. Dr. Saharjo No. 45, Manggarai",
    "email": "akawulamuda@gmail.com",
    "description": "Sanggar legendaris pimpinan Aditya Gumay, fokus akting dan tari.",
    "reviews": [ { "user": "Melly Goeslaw", "comment": "Paket komplit seni peran dan tari." } ]
  },
  {
    "sanggar_id": "ST020",
    "nama_sanggar": "Sanggar Ratna Sari",
    # Foto Topeng Close up
    "image": "https://images.unsplash.com/photo-1613963795550-934c99859267?q=80&w=800&auto=format&fit=crop",
    "phone_number": "-",
    "location": "Cimanggis, Depok",
    "email": "-",
    "description": "Salah satu sanggar Topeng Betawi tertua kelolaan keluarga H. Bokir.",
    "reviews": [ { "user": "Haringga", "comment": "Sangat otentik gaya topengnya." } ]
  }
]

def run_import():
    print("Mulai import data dengan Gambar STABIL (Unsplash/Wiki)...")
    
    # Hapus data lama agar bersih
    Sanggar.objects.all().delete()
    
    for item in data_json:
        sanggar = Sanggar.objects.create(
            sanggar_id=item['sanggar_id'],
            nama_sanggar=item['nama_sanggar'],
            image=item['image'], 
            phone_number=item['phone_number'],
            location=item['location'],
            email=item['email'],
            description=item['description']
        )
        print(f"Created: {sanggar.nama_sanggar}")

        for rev in item['reviews']:
            Review.objects.create(
                sanggar=sanggar,
                user=rev['user'],
                comment=rev['comment']
            )
    
    print("Selesai! Gambar seharusnya sudah muncul sekarang.")

if __name__ == '__main__':
    run_import()