# Generated by Django 5.1.6 on 2025-02-28 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_member_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='phone_number',
        ),
    ]
