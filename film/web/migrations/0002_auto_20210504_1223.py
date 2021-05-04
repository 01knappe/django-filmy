# Generated by Django 3.2 on 2021-05-04 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zanr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zanr', models.CharField(help_text='Zadejte text o maximální délce 20 znaků', max_length=20, unique=True, verbose_name='Žánr')),
            ],
            options={
                'ordering': ['zanr'],
            },
        ),
        migrations.AddField(
            model_name='film',
            name='rok',
            field=models.IntegerField(blank=True, null=True, verbose_name='Rok vydani'),
        ),
        migrations.AddField(
            model_name='film',
            name='stat',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Stát'),
        ),
        migrations.AlterField(
            model_name='film',
            name='nazev',
            field=models.CharField(max_length=50, verbose_name='Nazev'),
        ),
    ]
