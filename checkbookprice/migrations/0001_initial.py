# Generated by Django 4.2.2 on 2023-06-29 07:55

import checkbookprice.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=checkbookprice.models.user_path)),
            ],
        ),
    ]
