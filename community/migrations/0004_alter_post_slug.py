# Generated by Django 3.2.3 on 2021-06-11 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0003_rename_title_image_photo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=200),
        ),
    ]
