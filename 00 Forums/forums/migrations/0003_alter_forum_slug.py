# Generated by Django 4.0.4 on 2022-05-12 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0002_forum_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='slug',
            field=models.SlugField(editable=False, unique=True),
        ),
    ]
