# Generated by Django 5.0.4 on 2024-05-14 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0022_alter_music_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30, null=True)),
                ('Img', models.ImageField(null=True, upload_to='Podcast/')),
                ('Url', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]