# Generated by Django 4.2.3 on 2023-08-07 12:06

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Namanblogs', '0002_popularblogs_regularblogs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='popularblogs',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='regularblogs',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]