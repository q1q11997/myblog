# Generated by Django 2.0 on 2018-03-01 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180301_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='read_num',
            field=models.IntegerField(default=0, verbose_name='阅读人数'),
        ),
    ]
