# Generated by Django 3.2.3 on 2021-06-01 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_ayarlar_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ayarlar',
            name='IletisimAdres',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Adres'),
        ),
        migrations.AlterField(
            model_name='ayarlar',
            name='IletisimEposta',
            field=models.CharField(blank=True, max_length=75, null=True, verbose_name='E-posta Adresi'),
        ),
        migrations.AlterField(
            model_name='ayarlar',
            name='IletisimHarita',
            field=models.TextField(blank=True, verbose_name='Harita iFrame'),
        ),
        migrations.AlterField(
            model_name='ayarlar',
            name='IletisimTelefon',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefon'),
        ),
        migrations.AlterField(
            model_name='ayarlar',
            name='SiteAciklama',
            field=models.CharField(blank=True, max_length=160, null=True, verbose_name='Arama Motoru Açıklaması'),
        ),
        migrations.AlterField(
            model_name='ayarlar',
            name='SiteAnahtarKelimeler',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Arama Motoru Anahtar Kelimeler'),
        ),
    ]
