# Generated by Django 3.2.3 on 2021-06-02 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_haberler'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='haberler',
            name='KategoriID',
        ),
    ]
