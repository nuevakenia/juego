# Generated by Django 3.2.5 on 2022-01-11 03:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Arena',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Tienda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
                ('dialogo', models.CharField(max_length=300)),
            ],
        ),
        migrations.RemoveField(
            model_name='personaje',
            name='nivel',
        ),
        migrations.CreateModel(
            name='TiendaPrecios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.IntegerField(default=1)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tienda_precios_items', to='core.item')),
                ('tienda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tienda_precios_tiendas', to='core.tienda')),
            ],
        ),
        migrations.AddField(
            model_name='tienda',
            name='nivel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Tiendas', to='core.personaje'),
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
                ('jugador1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salas_jugador1', to='core.personaje')),
                ('jugador2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salas_jugador2', to='core.personaje')),
            ],
        ),
        migrations.CreateModel(
            name='Resultado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiempo', models.TimeField(blank=True, null=True)),
                ('puntaje1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resultados_puntaje1', to='core.personaje')),
                ('puntaje2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resultados_puntaje2', to='core.personaje')),
            ],
        ),
        migrations.CreateModel(
            name='PersonajeDetalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel', models.IntegerField(default=1)),
                ('exp', models.IntegerField(default=1)),
                ('vida', models.IntegerField(default=1)),
                ('energia', models.IntegerField(default=1)),
                ('fuerza', models.IntegerField(default=1)),
                ('destreza', models.IntegerField(default=1)),
                ('inteligencia', models.IntegerField(default=1)),
                ('personaje', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personaje_detalles', to='core.personaje')),
            ],
        ),
        migrations.CreateModel(
            name='Partida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arena', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partidas_arenas', to='core.arena')),
                ('jugador1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partidas_jugador1', to='core.personaje')),
                ('jugador2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partidas_jugador2', to='core.personaje')),
                ('resultado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partidas_resultados', to='core.resultado')),
            ],
        ),
        migrations.CreateModel(
            name='ItemDetalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('nivel', models.IntegerField(default=1)),
                ('sinergia1', models.IntegerField(blank=True, null=True)),
                ('sinergia2', models.IntegerField(blank=True, null=True)),
                ('sinergia3', models.IntegerField(blank=True, null=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items_detalles', to='core.item')),
            ],
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posicion', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventarios_items', to='core.item')),
                ('personaje', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventarios_personaje', to='core.personaje')),
            ],
        ),
        migrations.AddField(
            model_name='arena',
            name='jugador1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Arenas', to='core.personaje'),
        ),
        migrations.CreateModel(
            name='AccionDetalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acciones_detalles_accion', to='core.accion')),
                ('arena', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='acciones_detalles_arenas', to='core.arena')),
            ],
        ),
        migrations.AddField(
            model_name='accion',
            name='jugador1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Acciones', to='core.personaje'),
        ),
    ]
