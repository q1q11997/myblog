# Generated by Django 2.0 on 2018-05-16 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music_name', models.CharField(max_length=50, verbose_name='歌名')),
                ('music_word', models.CharField(max_length=100, verbose_name='歌词')),
                ('music_id', models.IntegerField(default=0, verbose_name='歌曲id')),
                ('singer', models.CharField(max_length=50, verbose_name='歌手')),
            ],
            options={
                'verbose_name': '歌曲',
                'verbose_name_plural': '歌曲',
            },
        ),
    ]
