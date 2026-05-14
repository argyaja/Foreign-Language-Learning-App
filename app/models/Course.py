from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    FLAG_ICON_CHOICES = sorted([
        ('flag-us', 'United States'),
        ('flag-cn', 'China'),
        ('flag-in', 'India'),
        ('flag-br', 'Brazil'),
        ('flag-ru', 'Russia'),
        ('flag-mx', 'Mexico'),
        ('flag-jp', 'Japan'),
        ('flag-de', 'Germany'),
        ('flag-fr', 'France'),
        ('flag-it', 'Italy'),
        ('flag-gb', 'United Kingdom'),
        ('flag-es', 'Spain'),
        ('flag-id', 'Indonesia'),
        ('flag-pk', 'Pakistan'),
        ('flag-bd', 'Bangladesh'),
        ('flag-ng', 'Nigeria'),
        ('flag-ph', 'Philippines'),
        ('flag-vn', 'Vietnam'),
        ('flag-ir', 'Iran'),
        ('flag-th', 'Thailand'),
        ('flag-tr', 'Turkey'),
        ('flag-eg', 'Egypt'),
        ('flag-et', 'Ethiopia'),
        ('flag-mm', 'Myanmar'),
        ('flag-za', 'South Africa'),
        ('flag-co', 'Colombia'),
        ('flag-ar', 'Argentina'),
        ('flag-pl', 'Poland'),
        ('flag-ca', 'Canada'),
        ('flag-sa', 'Saudi Arabia'),
    ], key=lambda x: x[1])

    LANGUAGE_CHOICES = [
        ('Bahasa Afrikaans (Afrika Selatan)'),
        ('Bahasa Arab'),
        ('Bahasa Bulgaria'),
        ('Bahasa Catalan (Spanyol)'),
        ('Bahasa Ceko'),
        ('Bahasa Denmark'),
        ('Bahasa Belanda'),
        ('Bahasa Inggris (Australia)'),
        ('Bahasa Inggris (Kanada)'),
        ('Bahasa Inggris (Inggris)'),
        ('Bahasa Inggris (India)'),
        ('Bahasa Selandia Baru'),
        ('Bahasa Inggris (Afrika Selatan)'),
        ('Bahasa Inggris (Amerika Serikat)'),
        ('Bahasa Finlandia'),
        ('Bahasa Kanada'),
        ('Bahasa Prancis'),
        ('Bahasa Jerman'),
        ('Bahasa Yunani'),
        ('Bahasa Israel'),
        ('Bahasa India'),
        ('Bahasa Hongaria'),
        ('Bahasa Indonesia'),
        ('Bahasa Italia'),
        ('Bahasa Jepang'),
        ('Bahasa Korea'),
        ('Bahasa Cina'),
        ('Bahasa Hong Kong'),
        ('Bahasa Taiwan'),
        ('Bahasa Norwegia'),
        ('Bahasa Polandia'),
        ('Bahasa Brasil'),
        ('Bahasa Portugal'),
        ('Bahasa Rumania'),
        ('Bahasa Rusia'),
        ('Bahasa Slowakia'),
        ('Bahasa Argentina'),
        ('Bahasa Chili'),
        ('Bahasa Kolombia'),
        ('Bahasa Meksiko'),
        ('Bahasa Spanyol'),
        ('Bahasa Swedia'),
        ('Bahasa Thailand'),
        ('Bahasa Turki'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255, choices=[(lang, lang) for lang in LANGUAGE_CHOICES])
    image = models.ImageField(upload_to='course_images/', null=True, blank=True)
    description = models.TextField()
    flag_icon = models.CharField(max_length=255, choices=FLAG_ICON_CHOICES, null=True, blank=True)
    
    def __str__(self):
        return self.name
