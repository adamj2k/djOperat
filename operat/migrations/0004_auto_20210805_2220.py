# Generated by Django 3.2.5 on 2021-08-05 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operat', '0003_auto_20210805_1926'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sprawozdanie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zakresMat', models.TextField(default='Po analizie materiałów pozyskanych z PZGiK do...')),
                ('techMet1', models.TextField(default='Wykonano pomiar ... ')),
                ('techMet2', models.TextField(default='elementy zostały pomierzone metodą ...')),
            ],
        ),
        migrations.AlterField(
            model_name='robota',
            name='wojew',
            field=models.CharField(default='zachodniopomorskie', max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='Spis',
        ),
        migrations.AddField(
            model_name='sprawozdanie',
            name='idpracy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='operat.robota'),
        ),
    ]
