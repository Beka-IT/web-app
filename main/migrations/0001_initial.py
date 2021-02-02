# Generated by Django 3.1.5 on 2021-01-26 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Films',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('premiere_year', models.IntegerField()),
                ('country', models.CharField(max_length=20)),
                ('genre', models.CharField(max_length=100)),
                ('duration', models.IntegerField()),
                ('producer', models.CharField(max_length=40)),
                ('cast', models.CharField(max_length=150)),
                ('picture_url', models.CharField(max_length=255)),
                ('video_url', models.CharField(max_length=255)),
                ('isSolo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='FutureFilms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('picture_url', models.CharField(max_length=255)),
            ],
        ),
    ]