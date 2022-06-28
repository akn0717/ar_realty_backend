# Generated by Django 4.0.4 on 2022-06-28 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0002_alter_realtor_photo'),
        ('properties', '0006_alter_property_cooling_alter_property_heating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='realtor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.realtor'),
        ),
    ]
