# Generated by Django 3.2.4 on 2023-07-02 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20230702_2312'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagesHome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images_home/')),
            ],
        ),
        migrations.DeleteModel(
            name='FooterLink',
        ),
        migrations.DeleteModel(
            name='NavLink',
        ),
    ]
