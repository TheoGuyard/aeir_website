# Generated by Django 3.0.1 on 2020-01-06 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("content", "0011_auto_20200106_1222"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="globalwebsiteparameters", name="sell_conditions",
        ),
    ]
