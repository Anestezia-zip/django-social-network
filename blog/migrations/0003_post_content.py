# Generated by Django 4.2.6 on 2023-10-31 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True, help_text='ffff', max_length=5000, null=True),
        ),
    ]
