# Generated by Django 3.1.3 on 2020-11-11 14:06

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=80)),
                ('message', models.TextField(max_length=500)),
            ],
        ),
    ]
