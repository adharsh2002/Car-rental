# Generated by Django 2.1 on 2022-01-27 07:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import system.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
                ('mssg', models.TextField()),
            ],
        ),
       
      
        migrations.CreateModel(
            name='PrivateMsg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]
