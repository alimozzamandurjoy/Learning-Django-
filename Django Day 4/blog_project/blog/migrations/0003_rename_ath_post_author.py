# Generated by Django 3.2.4 on 2021-06-09 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210609_1633'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='ath',
            new_name='author',
        ),
    ]
