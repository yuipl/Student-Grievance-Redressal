# Generated by Django 3.0.6 on 2020-06-23 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_auto_20200623_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='security_question',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='student',
            name='security_question',
            field=models.CharField(max_length=40),
        ),
    ]
