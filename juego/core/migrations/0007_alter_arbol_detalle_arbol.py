# Generated by Django 4.0.2 on 2022-02-11 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_arboldetalle_remove_inventario_item_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arbol',
            name='detalle_arbol',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='arbol_detalles', to='core.arboldetalle'),
        ),
    ]
