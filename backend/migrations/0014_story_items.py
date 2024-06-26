# Generated by Django 5.0.4 on 2024-05-13 06:30

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0013_alter_ona_items_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Story_Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ImgThumb', models.ImageField(null=True, upload_to='story/')),
                ('Title', models.CharField(max_length=20, null=True)),
                ('SubTitle', models.CharField(max_length=50, null=True)),
                ('Content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
            ],
        ),
    ]
