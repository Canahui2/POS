# Generated by Django 2.1.1 on 2018-10-29 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resoluciones', '0002_resolucion_operador'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resolucion',
            name='id',
        ),
        migrations.AlterField(
            model_name='resolucion',
            name='NumeroResolucion',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]