# Generated by Django 3.1 on 2021-11-10 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mmain', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopPlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=100)),
                ('place_img', models.ImageField(upload_to='dynamic_pic')),
                ('place_desc', models.TextField(max_length=50)),
            ],
        ),
    ]
