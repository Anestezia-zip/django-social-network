# Generated by Django 4.2.6 on 2023-11-29 10:19

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_region_options_alter_userprofile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/dyadwedsy/image/upload/v1701253087/volunteer/cvkvh8nqgn1m3hgmjmaz.png', max_length=255, verbose_name='image'),
        ),
    ]