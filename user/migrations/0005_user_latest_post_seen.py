# Generated by Django 3.2.7 on 2021-09-15 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20210915_0538'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='latest_post_seen',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
