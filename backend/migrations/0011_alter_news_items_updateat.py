# Generated by Django 5.0.4 on 2024-05-12 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_alter_news_items_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news_items',
            name='UpdateAt',
            field=models.DateField(),
        ),
    ]
