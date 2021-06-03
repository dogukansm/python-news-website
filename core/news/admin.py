from django.contrib import admin
from .models import Ayarlar, Haberler, Kategoriler, SonDakika, SosyalMedyaHesaplari, SosyalMedyaIkonlari

class AyarlarAdmin(admin.ModelAdmin):
    list_display = ['ID', 'SiteBaslik']
    list_display_links = ['ID']
    list_filter = ['ID']
    search_fields = ['ID', 'SiteBaslik', 'SiteAciklama', 'SiteAnahtarKelimeler']
    list_editable = ['SiteBaslik']

    class Meta:
        model = Ayarlar

class KategorilerAdmin(admin.ModelAdmin):
    list_display = ['ID', 'Baslik']
    list_display_links = ['ID']
    list_filter= ['ID']
    search_fields = ['ID', 'Baslik']
    list_editable = ['Baslik']

    class Meta:
        model = Kategoriler

class SonDakikaAdmin(admin.ModelAdmin):
    list_display = ['ID', 'Haber']
    list_display_links = ['ID']
    list_filter = ['ID']
    search_fields = ['ID', 'Haber']
    list_editable = ['Haber']

    class Meta:
        model = SonDakika

class SosyalMedyaIkonlariAdmin(admin.ModelAdmin):
    list_display = ['ID', 'IkonAdi', 'Ikon']
    list_display_links = ['ID']
    list_filter = ['ID']
    search_fields = ['ID', 'IkonAdi', 'Ikon']
    list_editable = ['IkonAdi', 'Ikon']

    class Meta:
        model = SosyalMedyaIkonlari

class SosyalMedyaHesaplariAdmin(admin.ModelAdmin):
    list_display = ['ID', 'Baslik', 'Adres']
    list_display_links = ['ID']
    list_filter = ['ID']
    search_fields = ['ID', 'Baslik', 'Adres']
    list_editable = ['Baslik', 'Adres']

    class Meta:
        model = SosyalMedyaHesaplari

class HaberlerAdmin(admin.ModelAdmin):
    list_display = ['ID', 'Baslik']
    list_display_links = ['ID']
    list_filter = ['ID']
    search_fields = ['ID', 'Baslik', 'Aciklama']
    
    class Meta:
        model = Haberler

admin.site.register(Ayarlar, AyarlarAdmin)
admin.site.register(Kategoriler, KategorilerAdmin)
admin.site.register(SonDakika, SonDakikaAdmin)
admin.site.register(SosyalMedyaIkonlari, SosyalMedyaIkonlariAdmin)
admin.site.register(SosyalMedyaHesaplari, SosyalMedyaHesaplariAdmin)
admin.site.register(Haberler, HaberlerAdmin)