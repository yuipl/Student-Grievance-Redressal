# Generated by Django 3.0.6 on 2020-06-06 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complain', '0008_auto_20200605_1412'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complain',
            old_name='complainee',
            new_name='complainer',
        ),
        migrations.AddField(
            model_name='complain',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='complain/'),
        ),
    ]
