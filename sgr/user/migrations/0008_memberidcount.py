# Generated by Django 3.0.6 on 2020-06-22 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20200622_0844'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberIDCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_id', models.IntegerField()),
            ],
        ),
    ]
