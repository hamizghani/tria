from django.contrib import admin
from .models import Sanggar, Review

# Opsi 1: Tampilan standar
# admin.site.register(Sanggar)
# admin.site.register(Review)

# Opsi 2: Tampilan lebih canggih (Inline Review di dalam Sanggar)
class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1

@admin.register(Sanggar)
class SanggarAdmin(admin.ModelAdmin):
    list_display = ('sanggar_id', 'nama_sanggar', 'location', 'phone_number')
    search_fields = ('nama_sanggar', 'location')
    inlines = [ReviewInline] # Ini bikin kita bisa nambah review langsung di halaman edit sanggar

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'sanggar', 'comment')