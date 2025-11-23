from django.db import models

class Sanggar(models.Model):
    sanggar_id = models.CharField(max_length=10, unique=True, primary_key=True)
    nama_sanggar = models.CharField(max_length=200)
    
    
    image= models.URLField(max_length=200, blank=True, null=True) 
    
    
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    location = models.TextField()
    email = models.EmailField(blank=True, null=True)
    description = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nama_sanggar

    @property
    def wa_link(self):
        if not self.phone_number or self.phone_number == '-':
            return "#"
        
        clean_num = ''.join(filter(str.isdigit, self.phone_number))
        
        if not clean_num:
            return "#"

        if clean_num.startswith('0'):
            wa_num = '62' + clean_num[1:]
        elif clean_num.startswith('62'):
            wa_num = clean_num
        else:
            wa_num = '62' + clean_num 

        text = f"Halo {self.nama_sanggar}, saya ingin bertanya info pendaftaran."
        return f"https://wa.me/{wa_num}?text={text}"


class Review(models.Model):
    sanggar = models.ForeignKey(Sanggar, on_delete=models.CASCADE, related_name='reviews')
    user = models.CharField(max_length=100)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.sanggar.nama_sanggar}"