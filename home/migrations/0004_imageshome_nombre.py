# Generated by Django 3.2.4 on 2023-07-02 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20230702_2318'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageshome',
            name='nombre',
            field=models.SlugField(blank=True, null=True),
        ),
    ]