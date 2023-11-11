# Generated by Django 4.2.6 on 2023-11-10 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='left_position',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='region',
            name='top_position',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]