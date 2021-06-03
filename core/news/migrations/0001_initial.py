# Generated by Django 3.2.3 on 2021-06-01 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ayarlar',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('LogoNegatif', models.ImageField(blank=True, null=True, upload_to='core')),
                ('LogoPozitif', models.ImageField(blank=True, null=True, upload_to='core')),
                ('SiteIkon', models.ImageField(blank=True, null=True, upload_to='core')),
                ('SiteBaslik', models.CharField(max_length=60, verbose_name='Site Tarayıcı Başlığı')),
                ('SiteAciklama', models.CharField(max_length=160, null=True, verbose_name='Arama Motoru Açıklaması')),
                ('SiteAnahtarKelimeler', models.CharField(max_length=200, null=True, verbose_name='Arama Motoru Anahtar Kelimeler')),
                ('IletisimAdres', models.CharField(max_length=200, null=True, verbose_name='Adres')),
                ('IletisimTelefon', models.CharField(max_length=20, null=True, verbose_name='Telefon')),
                ('IletisimEposta', models.CharField(max_length=75, null=True, verbose_name='E-posta Adresi')),
                ('IletisimHarita', models.TextField(verbose_name='Harita iFrame')),
            ],
            options={
                'ordering': ['ID'],
            },
        ),
    ]