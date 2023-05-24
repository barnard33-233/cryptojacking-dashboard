# Generated by Django 4.1 on 2023-05-24 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceRecord',
            fields=[
                ('mac', models.CharField(max_length=17, primary_key=True, serialize=False)),
                ('ip', models.CharField(max_length=15)),
                ('safety', models.IntegerField(choices=[(0, 'SAFE'), (1, 'DANGEROUS')], default=0)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Modified',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mtime', models.DateTimeField()),
            ],
        ),
    ]
