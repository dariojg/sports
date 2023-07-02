# Generated by Django 3.2.4 on 2023-07-01 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('club', models.CharField(max_length=100)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='jugadores/')),
                ('fecha_nacimiento', models.DateField()),
                ('nacionalidad', models.CharField(max_length=100)),
                ('Posicion', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Estadistica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_estadisitca', models.CharField(choices=[('Pases', 'Pases'), ('Goles', 'Goles'), ('Partidos Jugados', 'Partidos Jugados'), ('Penales acertados', 'Penales acertados'), ('Penales errados', 'Penales errados'), ('Penales Atajados', 'Penales Atajados')], max_length=50)),
                ('jugador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jugadores.jugador')),
            ],
        ),
    ]