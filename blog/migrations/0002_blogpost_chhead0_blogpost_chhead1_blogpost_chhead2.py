# Generated by Django 4.1.4 on 2023-01-06 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='chhead0',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='chhead1',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='chhead2',
            field=models.CharField(default='', max_length=5000),
        ),
    ]
