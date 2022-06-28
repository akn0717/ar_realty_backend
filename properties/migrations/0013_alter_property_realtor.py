# Generated by Django 4.0.4 on 2022-06-28 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0002_alter_realtor_photo'),
        ('properties', '0012_alter_property_realtor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='realtor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='realtors.realtor'),
        ),
    ]
