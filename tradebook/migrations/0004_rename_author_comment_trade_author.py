# Generated by Django 4.2.2 on 2023-06-30 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tradebook', '0003_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='trade_author',
        ),
    ]
