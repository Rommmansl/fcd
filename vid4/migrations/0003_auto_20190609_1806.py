# Generated by Django 2.2.1 on 2019-06-09 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vid4', '0002_auto_20190609_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='picfile',
            field=models.ImageField(upload_to=''),
        ),
    ]
