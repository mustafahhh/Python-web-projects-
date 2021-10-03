# Generated by Django 3.2.6 on 2021-09-19 11:51

from django.db import migrations, models
import web.helpers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=15)),
                ('image', models.ImageField(upload_to=web.helpers.RandomFileName('files'))),
                ('token', models.CharField(default='BasicToken-77a17880-6ad9-47d2-99c2-3eea43445b6bbde58711-7b6d-4f5b-b3ca-1ac329c9f800', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomid', models.CharField(max_length=6)),
                ('message', models.TextField(blank=True, max_length=64)),
                ('user', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomid', models.CharField(max_length=6)),
                ('usersconnected', models.TextField()),
            ],
        ),
    ]