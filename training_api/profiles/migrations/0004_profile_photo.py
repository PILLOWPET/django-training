# Generated by Django 3.0.3 on 2020-06-04 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_profile_following_profiles'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='photo',
            field=models.FileField(blank=True, default='', upload_to=''),
        ),
    ]
