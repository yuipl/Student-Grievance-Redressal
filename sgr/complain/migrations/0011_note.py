# Generated by Django 3.0.6 on 2020-06-17 15:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_student_admission_type'),
        ('complain', '0010_auto_20200606_2044'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField()),
                ('file', models.FileField(blank=True, null=True, upload_to='note/')),
                ('reg_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('complain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='complain.Complain')),
                ('solver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Member')),
            ],
        ),
    ]
