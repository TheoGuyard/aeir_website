# Generated by Django 2.2.1 on 2019-09-30 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adhesion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adhesion',
            name='picture',
            field=models.ImageField(upload_to=''),
        ),
    ]
