# Generated by Django 3.2.5 on 2021-07-08 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userface',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='users/')),
            ],
        ),
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.IntegerField(choices=[(1, 'Rov1'), (2, 'Rov2'), (3, 'Rov3'), (4, 'Van1'), (5, 'Van2'), (6, 'Van3'), (7, 'And1'), (8, 'And2'), (9, 'And3'), (10, 'Jak1'), (11, 'Jak2'), (12, 'Jak3'), (13, 'Frn1'), (14, 'Frn2'), (15, 'Frn3'), (16, 'Pic1'), (17, 'Pic2'), (18, 'Pic3')])),
                ('sample', models.ImageField(upload_to='images/')),
                ('img1', models.ImageField(default=None, null=True, upload_to='images/')),
                ('img2', models.ImageField(default=None, null=True, upload_to='images/')),
                ('img3', models.ImageField(default=None, null=True, upload_to='images/')),
                ('face', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vars', to='painter.userface')),
            ],
        ),
    ]