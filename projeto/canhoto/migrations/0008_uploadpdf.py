# Generated by Django 4.1.7 on 2023-04-08 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canhoto', '0007_canhoto_conferencia'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadPdf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='scanning_pdfs/')),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
