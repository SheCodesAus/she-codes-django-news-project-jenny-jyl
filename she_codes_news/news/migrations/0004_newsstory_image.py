# Generated by Django 4.1.3 on 2022-12-10 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_newsstory_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsstory',
            name='image',
            field=models.URLField(default=''),
        ),
    ]
