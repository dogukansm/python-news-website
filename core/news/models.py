from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from djrichtextfield.models import RichTextField

class Ayarlar(models.Model):
    ID = models.AutoField(primary_key=True, editable=False)
    LogoNegatif = models.ImageField(null=True, blank=True, upload_to="core")
    LogoPozitif = models.ImageField(null=True, blank=True, upload_to="core")
    SiteIkon = models.ImageField(null=True, blank=True, upload_to="core")
    SiteBanner = models.ImageField(null=True, blank=True, upload_to="core")
    SiteBaslik = models.CharField(max_length=60, null=False, verbose_name="Site Tarayıcı Başlığı")
    SiteAciklama = models.CharField(max_length=160, null=True, blank=True, verbose_name="Arama Motoru Açıklaması")
    SiteAnahtarKelimeler = models.CharField(max_length=200, null=True, blank=True, verbose_name="Arama Motoru Anahtar Kelimeler")
    SiteCopyright = models.CharField(max_length = 300, null=False, blank=False, default="Copyright ©", verbose_name="Site Altında Gözüken Copyright Yazısı")
    IletisimAdres = models.CharField(max_length=200, null=True, blank=True, verbose_name="Adres")
    IletisimTelefon = models.CharField(max_length=20, null=True, blank=True, verbose_name="Telefon")
    IletisimEposta = models.CharField(max_length=75, null=True, blank=True, verbose_name="E-posta Adresi")
    IletisimHarita = models.TextField(verbose_name="Harita iFrame", blank=True)

    def __str__(self):
        return self.SiteBaslik

    class Meta:
        ordering = ['ID']
        verbose_name = _("Ayarlar")
        verbose_name_plural = _("Ayarlar")

class Kategoriler(models.Model):
    ID = models.AutoField(primary_key=True, editable=False)
    Baslik = models.CharField(max_length=120, null=False, blank=False, verbose_name="Kategori Başlık")
    Aciklama = models.TextField(verbose_name="Kategori Açıklama", blank=True)

    def __str__(self):
        return self.Baslik

    def get_absolute_url(self):
        return reverse("kategoriler", kwargs={"ID": self.ID})
    

    class Meta:
        ordering = ['ID']
        verbose_name = _('Kategoriler')
        verbose_name_plural = _('Kategoriler')

class SonDakika(models.Model):
    ID = models.AutoField(primary_key=True, editable=False)
    Haber = models.TextField(verbose_name="Haber İçeriği", blank=False)

    def __str__(self):
        return self.Haber

    class Meta:
        ordering = ['ID']
        verbose_name = _('Son Dakika Haberleri')
        verbose_name_plural = _('Son Dakika Haberleri')

class SosyalMedyaIkonlari(models.Model):
    ID = models.AutoField(primary_key=True, editable=False)
    IkonAdi = models.CharField(max_length=120, null=False, blank=False, verbose_name="İkon Adı")
    Ikon = models.CharField(max_length=120, null=False, blank=False, verbose_name="İkon")

    def __str__(self):
        return self.IkonAdi

    class Meta:
        ordering = ['ID']
        verbose_name = _('Sosyal Medya İkon Tanımları')
        verbose_name_plural = _('Sosyal Medya İkon Tanımları')

class SosyalMedyaHesaplari(models.Model):
    ID = models.AutoField(primary_key=True, editable=False)
    IkonID = models.OneToOneField(SosyalMedyaIkonlari, unique=True, on_delete=models.CASCADE)
    Baslik = models.CharField(max_length=120, null=False, blank=False, verbose_name="Başlık")
    Adres = models.CharField(max_length=500, null=False, blank=False, verbose_name="URL")

    def __str__(self):
        return self.Baslik

    class Meta:
        ordering = ['ID']
        verbose_name = _('Sosyal Medya Hesap Tanımları')
        verbose_name_plural = _('Sosyal Medya Hesap Tanımları')

class Haberler(models.Model):
    ID = models.AutoField(primary_key=True, editable=False)
    KategoriID = models.ForeignKey(Kategoriler, unique=False, on_delete=models.CASCADE)
    Baslik = models.CharField(max_length=120, null=False, blank=False, verbose_name="Haber Başlık")
    Aciklama = models.TextField(verbose_name="Haber Açıklama", blank=True)
    Icerik = RichTextField()
    Resim = models.ImageField(null=True, blank=True, upload_to="news")
    SliderAlani = models.BooleanField(verbose_name="Slider Alanında Gözüksün mü?")
    YayinlanmaTarihi = models.DateTimeField(verbose_name="Yayınlanma Tarihi", auto_now_add=True, editable=False)

    def __str__(self):
        return self.Baslik

    def get_absolute_url(self):
        return reverse("haberler", kwargs={"ID": self.ID})

    class Meta:
        ordering = ['ID']
        verbose_name = _('Haberler')
        verbose_name_plural = _('Haberler')
