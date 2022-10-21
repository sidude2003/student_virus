# Generated by Django 4.1.2 on 2022-10-15 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('homepage', '0002_delete_students'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll', models.IntegerField()),
                ('name', models.CharField(max_length=64)),
                ('gender', models.CharField(max_length=6)),
                ('branch', models.CharField(max_length=5)),
                ('section', models.CharField(max_length=5)),
            ],
        ),
    ]
