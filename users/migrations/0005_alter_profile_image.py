# Generated by Django 4.1.4 on 2023-08-25 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='images/profile_pictures/profilepic.jpg', upload_to='images/profile_pictures'),
        ),
    ]
