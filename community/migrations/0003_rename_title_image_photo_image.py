# Generated by Django 3.2.3 on 2021-06-01 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_auto_20210602_0350'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='title_image',
            new_name='image',
        ),
    ]