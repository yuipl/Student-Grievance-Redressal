# Generated by Django 3.0.6 on 2020-06-06 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20200605_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='security_answer',
            field=models.CharField(default='What is your name?', max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='security_question',
            field=models.CharField(default='ala ', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='security_answer',
            field=models.CharField(default='ahakja', max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='security_question',
            field=models.CharField(default='qjq', max_length=30),
            preserve_default=False,
        ),
    ]
