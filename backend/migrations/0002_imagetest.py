# Generated by Django 5.0.4 on 2024-05-04 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Img', models.ImageField(null=True, upload_to='carousels/')),
                ('description', models.CharField(max_length=200, null=True)),
                ('alt', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
