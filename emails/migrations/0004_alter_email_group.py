# Generated by Django 3.2.1 on 2021-05-08 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
        ('emails', '0003_alter_email_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='group',
            field=models.ManyToManyField(blank=True, to='groups.Group'),
        ),
    ]