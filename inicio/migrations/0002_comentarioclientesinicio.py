# Generated by Django 3.1.1 on 2020-10-08 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComentarioClientesInicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.FileField(upload_to='inicio/images/clientes/')),
                ('nombre', models.CharField(max_length=50)),
                ('comentario', models.TextField(max_length=350)),
            ],
        ),
    ]