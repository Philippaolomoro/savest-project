# Generated by Django 3.1 on 2020-08-26 17:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('savestpages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='creation_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default=0, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]