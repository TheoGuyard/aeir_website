# Generated by Django 3.0.1 on 2020-01-12 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("adhesion", "0008_auto_20200105_1601"),
        ("administration", "0006_auto_20191201_1350"),
    ]

    operations = [
        migrations.AlterField(
            model_name="eventmanagement",
            name="participants",
            field=models.ManyToManyField(blank=True, default=0, to="adhesion.Adhesion"),
        ),
    ]
