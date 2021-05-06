# Generated by Django 3.2.1 on 2021-05-06 10:54

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('email_messages', '0001_initial'),
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, default='', null=True)),
                ('status', models.IntegerField(choices=[(1, 'waiting'), (2, 'processing'), (3, 'done'), (4, 'fail')], default=1, editable=False, max_length=1)),
                ('term', models.DateTimeField(auto_now=True)),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='groups.group')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='email_messages.message')),
            ],
        ),
    ]
