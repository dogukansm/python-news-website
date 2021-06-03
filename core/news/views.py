from typing import ContextManager
from django.shortcuts import get_object_or_404, render
from .models import Haberler, Kategoriler, SonDakika, Ayarlar, SosyalMedyaHesaplari

def index(request):
    context = dict()
    context["ayarlar"] = Ayarlar.objects.filter(ID = 1)[:1].get()
    context["sondakikahaberleri"] = SonDakika.objects.all()
    context["sosyalmedyahesaplari"] = SosyalMedyaHesaplari.objects.all()
    context["kategoriler"] = Kategoriler.objects.all()
    context["slideralani"] = reversed(Haberler.objects.all().filter(SliderAlani = True).order_by('ID')[:10])
    context["slideralani2"] = reversed(Haberler.objects.all().filter(SliderAlani = True).order_by('ID')[:10])
    context["slideryanihaberler"] = reversed(Haberler.objects.all().filter(SliderAlani = True).order_by('ID')[10:15])
    context["saglikhaberleri"] = reversed(Haberler.objects.all().filter(KategoriID = 6).order_by('ID')[:10])
    context["teknolojihaberlerislider"] = reversed(Haberler.objects.all().filter(KategoriID = 5).order_by('ID')[:3])
    context["teknolojihaberleri1"] = reversed(Haberler.objects.all().filter(KategoriID = 5).order_by('ID')[3:6])
    context["teknolojihaberleri2"] = reversed(Haberler.objects.all().filter(KategoriID = 5).order_by('ID')[6:9])
    context["ekonomihaberleri"] = reversed(Haberler.objects.all().filter(KategoriID = 2).order_by('ID')[:3])

    return render(request, 'index.html', context)

def kategoriler(request, id):
    context = dict()
    context["kategorilericerik"] = reversed(Haberler.objects.all().filter(KategoriID = id))
    context["ayarlar"] = Ayarlar.objects.filter(ID = 1)[:1].get()
    context["sondakikahaberleri"] = SonDakika.objects.all()
    context["sosyalmedyahesaplari"] = SosyalMedyaHesaplari.objects.all()
    context["kategoriler"] = Kategoriler.objects.all()
    context["kategoridetay"] = Kategoriler.objects.filter(ID = id)[:1].get()
    context["gundemilk"] = reversed(Haberler.objects.all().filter(SliderAlani = True).order_by('ID')[:1])
    context["gundemuclu"] = reversed(Haberler.objects.all().filter(SliderAlani = True).order_by('ID')[1:4])
    
    return render(request, 'category.html', context)

def haberler(request, id):
    context = dict()
    context["ayarlar"] = Ayarlar.objects.filter(ID = 1)[:1].get()
    context["sondakikahaberleri"] = SonDakika.objects.all()
    context["sosyalmedyahesaplari"] = SosyalMedyaHesaplari.objects.all()
    context["kategoriler"] = Kategoriler.objects.all()
    context["haberdetay"] = Haberler.objects.filter(ID = id)[:1].get()
    context["gundemilk"] = reversed(Haberler.objects.all().filter(SliderAlani = True).order_by('ID')[:1])
    context["gundemuclu"] = reversed(Haberler.objects.all().filter(SliderAlani = True).order_by('ID')[1:4])

    return render(request, 'news.html', context)