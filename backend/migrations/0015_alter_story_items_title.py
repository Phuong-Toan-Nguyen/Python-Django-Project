# Generated by Django 5.0.4 on 2024-05-13 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0014_story_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story_items',
            name='Title',
            field=models.CharField(max_length=30, null=True),
        ),
    ]