# Generated by Django 4.0.1 on 2022-02-09 01:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0005_remove_personajedetalle_personaje_personaje_detalle'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArbolDetalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suerte', models.IntegerField(default=1)),
                ('agilidad', models.IntegerField(default=1)),
                ('carisma', models.IntegerField(default=1)),
                ('inteligencia', models.IntegerField(default=1)),
                ('fuerza', models.IntegerField(default=1)),
                ('percepcion', models.IntegerField(default=1)),
                ('resistencia', models.IntegerField(default=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='inventario',
            name='item',
        ),
        migrations.RemoveField(
            model_name='inventario',
            name='posicion',
        ),
        migrations.AddField(
            model_name='inventario',
            name='numero_casilleros',
            field=models.IntegerField(default=1),
        ),
        migrations.CreateModel(
            name='InventarioDetalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posx', models.IntegerField(default=1)),
                ('posy', models.IntegerField(default=1)),
                ('posz', models.IntegerField(default=1)),
                ('tam', models.IntegerField(default=1)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventario_detalles', to='core.item')),
            ],
        ),
        migrations.CreateModel(
            name='Arbol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalle_arbol', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='arbol_detalles', to='core.personajedetalle')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arbol_users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='inventario',
            name='arreglo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='inventarios_arreglo', to='core.inventariodetalle'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personaje',
            name='arbol',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='personajes_arbol', to='core.arbol'),
            preserve_default=False,
        ),
    ]
