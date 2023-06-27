# Generated by Django 4.2.2 on 2023-06-26 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_remove_goods_url_goods_image_goods_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goods',
            old_name='bname',
            new_name='name',
        ),
        migrations.AddField(
            model_name='goods',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='goods',
            name='image',
            field=models.ImageField(blank=True, upload_to='goods/%Y/%m/%d'),
        ),
    ]