# Generated by Django 2.0 on 2020-12-18 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Archive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object', models.CharField(max_length=100)),
                ('specialist', models.CharField(max_length=100)),
                ('date', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Production',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialist', models.CharField(max_length=100)),
                ('object', models.CharField(max_length=100)),
                ('term', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Specialists',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialist', models.CharField(max_length=100)),
                ('skills', models.IntegerField(default=0)),
                ('age', models.IntegerField(default=0)),
                ('car', models.CharField(max_length=100)),
            ],
        ),
    ]

