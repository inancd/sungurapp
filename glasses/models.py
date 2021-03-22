from django.db import models

# Create your models here.

class HomeModels(models.Model):
    title = models.CharField(max_length=255, verbose_name="Başlık")
    slider = models.ImageField(blank=True, null=True, verbose_name="Resim")
    date_pub = models.DateTimeField('Date Published', auto_now_add=True)
    number = models.IntegerField(verbose_name='Numara')

    class Meta:
        verbose_name_plural = 'Slider Ayarları'

    def __str__(self):
        return self.title


class AboutModels(models.Model):
    title = models.CharField(max_length=255, verbose_name="Resim")
    description = models.TextField(verbose_name="İçerik")
    image = models.ImageField(blank=True, null=True, upload_to='about/', verbose_name="Resim")
    date_pub = models.DateTimeField('Date Published', auto_now_add=True)

    class Meta:
        verbose_name_plural = "Hakkımızda"

    def __str__(self):
        return self.title

class BrandsModel(models.Model):
    title = models.CharField(max_length=255, verbose_name="başlık")
    image = models.ImageField(null=True, upload_to='brands', verbose_name="Resim")
    number = models.IntegerField(verbose_name="Numara")
    date_pub = models.DateTimeField('Date Published', auto_now_add=True)

    class Meta:
        verbose_name_plural = "Markalazımız"

    def __str__(self):
        return self.title

class GalleryModels(models.Model):
    title = models.CharField(max_length=255, null=False, verbose_name="başlık")
    image = models.ImageField(blank=True, null=True, upload_to='gallery', verbose_name="Resim")
    date_pub = models.DateTimeField('Date Published', auto_now_add=True)

    class Meta:
        verbose_name_plural = "Galeri"

    def __str__(self):
        return self.title

class StoreModel(models.Model):
    title = models.CharField(max_length=255, verbose_name="Başlık")
    adres = models.CharField(max_length=255, verbose_name="Adres")
    telefon = models.CharField(max_length=255, verbose_name="Telefon")
    email = models.CharField(max_length=255, verbose_name="Email Adresi")
    calisma_saatleri = models.CharField(max_length=255)
    maps = models.CharField(max_length=255, verbose_name="Harita")

    class Meta:
        verbose_name_plural = "Mağazalar"

    def __str__(self):
        return self.title

class StoreGalleryModels(models.Model):
    title = models.CharField(max_length=255, verbose_name="Başlık")
    magaza = models.ForeignKey(StoreModel, on_delete=models.CASCADE, verbose_name="Mağaza")
    image = models.ImageField(blank=True, null=True, upload_to='store', verbose_name="Resim")

    class Meta:
        verbose_name_plural = "Mağaza Resimleri"

    def __str__(self):
        return self.title

class TechnologyModels(models.Model):
    title = models.CharField(max_length=255, null=False, verbose_name="Başlık")
    image = models.ImageField(blank=True, null=True, upload_to='gallery', verbose_name="Resim")
    date_pub = models.DateTimeField('Date Published', auto_now_add=True)

    class Meta:
        verbose_name_plural = "Teknoloji Resimleri"

    def __str__(self):
        return self.title

class TechnologyDesModels(models.Model):
    title = models.CharField(max_length=255, verbose_name="Başlık")
    description = models.TextField(verbose_name="İçerik")
    date_pub = models.DateTimeField("Data Published", auto_now_add=True)

    class Meta:
        verbose_name_plural = "Teknoloji İçerik"

    def __str__(self):
        return self.title

