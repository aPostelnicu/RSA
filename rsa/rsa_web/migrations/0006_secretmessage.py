# Generated by Django 3.0.11 on 2021-01-05 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rsa_web', '0005_delete_secretmessage'),
    ]

    operations = [
        migrations.CreateModel(
            name='SecretMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
            ],
        ),
    ]
