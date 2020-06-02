# Generated by Django 3.0 on 2020-06-02 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.AddField(
            model_name='profile',
            name='description',
            field=models.CharField(default=' ', max_length=512),
            preserve_default=False,
        ),
    ]