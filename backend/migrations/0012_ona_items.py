# Generated by Django 5.0.4 on 2024-05-13 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0011_alter_news_items_updateat'),
    ]

    operations = [
        migrations.CreateModel(
            name='OnA_Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=20)),
                ('Date', models.DateField(null=True)),
                ('Detail', models.CharField(max_length=20)),
            ],
        ),
    ]
