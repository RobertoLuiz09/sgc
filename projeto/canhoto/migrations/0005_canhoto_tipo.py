# Generated by Django 4.1.7 on 2023-03-15 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canhoto', '0004_remove_canhoto_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='canhoto',
            name='tipo',
            field=models.CharField(default='', max_length=100),
        ),
    ]
