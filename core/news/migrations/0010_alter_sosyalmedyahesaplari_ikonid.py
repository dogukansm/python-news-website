# Generated by Django 3.2.3 on 2021-06-01 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_sosyalmedyahesaplari'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sosyalmedyahesaplari',
            name='IkonID',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='news.sosyalmedyaikonlari'),
        ),
    ]
