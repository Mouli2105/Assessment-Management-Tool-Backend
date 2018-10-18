# Generated by Django 2.1.2 on 2018-10-18 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tool', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='applicants',
            field=models.ManyToManyField(blank=True, to='Tool.Student'),
        ),
        migrations.AlterField(
            model_name='course',
            name='mentors',
            field=models.ManyToManyField(blank=True, to='Tool.Mentor'),
        ),
    ]
