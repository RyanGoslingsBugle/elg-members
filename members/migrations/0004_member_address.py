# Generated by Django 2.2 on 2019-04-15 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_member_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='address',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
