# Generated by Django 5.0.4 on 2024-04-15 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_author_image_post_image_post_view_count_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='phone',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]