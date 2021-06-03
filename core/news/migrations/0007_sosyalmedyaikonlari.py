# Generated by Django 3.2.3 on 2021-06-01 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_sondakika'),
    ]

    operations = [
        migrations.CreateModel(
            name='SosyalMedyaIkonlari',
            fields=[
                ('ID', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('IkonAdi', models.CharField(max_length=120, verbose_name='İkon Adı')),
                ('Ikon', models.CharField(max_length=120, verbose_name='İkon')),
            ],
            options={
                'verbose_name': 'Sosyal Medya İkon Tanımları',
                'ordering': ['ID'],
            },
        ),
    ]