# Generated by Django 3.2.3 on 2021-06-20 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0005_alter_photo_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='community.post'),
        ),
    ]
