# Generated by Django 2.0 on 2018-01-27 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='music',
            options={'verbose_name': '歌曲', 'verbose_name_plural': '歌曲'},
        ),
        migrations.AlterField(
            model_name='music',
            name='music_url',
            field=models.URLField(verbose_name='歌曲地址'),
        ),
    ]
