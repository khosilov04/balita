# Generated by Django 5.0.6 on 2024-05-21 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_alter_post_category_alter_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='is_banner',
        ),
    ]
