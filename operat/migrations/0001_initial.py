# Generated by Django 3.2 on 2021-04-30 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Robota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idpracy', models.CharField(max_length=15)),
                ('wojew', models.CharField(max_length=50)),
                ('data_operat', models.DateField(verbose_name='data operatu')),
            ],
        ),
        migrations.CreateModel(
            name='Spis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pozycja', models.CharField(max_length=200)),
                ('robota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operat.robota')),
            ],
        ),
    ]
