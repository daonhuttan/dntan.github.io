# Generated by Django 2.2.7 on 2021-04-04 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210328_2228'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='commend',
            new_name='comment', 
        ),
    ]
