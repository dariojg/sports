# Generated by Django 3.2.4 on 2023-07-02 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_imageshome_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageshome',
            name='type',
            field=models.CharField(choices=[('footer', 'footer'), ('feader', 'header'), ('nav', 'nav')], max_length=50, null=True),
        ),
    ]
