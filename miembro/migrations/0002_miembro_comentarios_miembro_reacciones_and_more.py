# Generated by Django 4.1.7 on 2023-04-17 02:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realiza', '0001_initial'),
        ('comentarios', '0001_initial'),
        ('reacciones', '0001_initial'),
        ('miembro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='miembro',
            name='comentarios',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='comentarios.comentarios'),
        ),
        migrations.AddField(
            model_name='miembro',
            name='reacciones',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reacciones.reacciones'),
        ),
        migrations.AddField(
            model_name='miembro',
            name='realiza',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='realiza.realiza'),
        ),
    ]
