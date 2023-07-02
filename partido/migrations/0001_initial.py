# Generated by Django 3.2.4 on 2023-07-01 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_local', models.CharField(max_length=100)),
                ('club_visitante', models.CharField(max_length=100)),
                ('imagen_escudo', models.ImageField(blank=True, null=True, upload_to='escudos/')),
                ('fecha_partido', models.DateField()),
                ('club', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Formacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posicion', models.CharField(max_length=30)),
                ('nombre_jugador', models.CharField(max_length=100)),
                ('club', models.CharField(max_length=30)),
                ('partido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='partido.partido')),
            ],
        ),
    ]