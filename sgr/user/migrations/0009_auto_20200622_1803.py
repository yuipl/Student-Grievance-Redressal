# Generated by Django 3.0.6 on 2020-06-22 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_memberidcount'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='member',
            options={},
        ),
        migrations.RenameField(
            model_name='memberidcount',
            old_name='last_id',
            new_name='next_id',
        ),
    ]
