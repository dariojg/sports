# Generated by Django 3.2.4 on 2023-07-02 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='footerlink',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='footer/'),
        ),
        migrations.AddField(
            model_name='navlink',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='nav/'),
        ),
    ]
