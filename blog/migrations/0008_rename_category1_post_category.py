# Generated by Django 3.2.6 on 2021-08-24 23:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_post_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='category1',
            new_name='category',
        ),
    ]
