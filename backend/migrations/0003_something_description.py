# Generated by Django 5.0.4 on 2024-05-04 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_imagetest'),
    ]

    operations = [
        migrations.AddField(
            model_name='something',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
