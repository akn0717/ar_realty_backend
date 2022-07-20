# Generated by Django 4.0.4 on 2022-07-18 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_businessinquiry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='businessinquiry',
            name='user_id',
        ),
        migrations.AddField(
            model_name='businessinquiry',
            name='company_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
