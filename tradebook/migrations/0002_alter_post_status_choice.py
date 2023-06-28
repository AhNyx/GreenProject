# Generated by Django 4.2.2 on 2023-06-22 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradebook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status_choice',
            field=models.CharField(choices=[('waiting', '판매대기'), ('buying', '거래중'), ('selling', '판매중'), ('finish', '거래종료')], default='waiting', max_length=10),
        ),
    ]