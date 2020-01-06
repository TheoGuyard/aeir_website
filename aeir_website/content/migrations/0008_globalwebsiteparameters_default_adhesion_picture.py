# Generated by Django 3.0.1 on 2020-01-05 20:01

from django.db import migrations
import stdimage.models
import stdimage.validators


class Migration(migrations.Migration):

    dependencies = [
        ("content", "0007_globalwebsiteparameters"),
    ]

    operations = [
        migrations.AddField(
            model_name="globalwebsiteparameters",
            name="default_adhesion_picture",
            field=stdimage.models.StdImageField(
                default=None,
                upload_to="global_parameters",
                validators=[
                    stdimage.validators.MinSizeValidator(230, 292),
                    stdimage.validators.MaxSizeValidator(1080, 720),
                ],
            ),
        ),
    ]
