# Generated by Django 5.1 on 2024-08-29 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matheus', '0002_rename_imagem_hobbie_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Namorado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
                ('idade', models.DateField()),
                ('nota', models.IntegerField()),
                ('sobre', models.CharField(max_length=300)),
            ],
        ),
    ]
