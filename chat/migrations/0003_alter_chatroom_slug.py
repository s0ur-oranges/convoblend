# Generated by Django 4.1.4 on 2023-08-16 13:27

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_chatmessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroom',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from=('name',), unique=True, verbose_name='slug'),
        ),
    ]
