# Generated by Django 4.0.4 on 2022-05-29 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=100, null=True),
        ),
    ]