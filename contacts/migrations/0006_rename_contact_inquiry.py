# Generated by Django 4.0.4 on 2022-07-12 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_alter_contact_message'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact',
            new_name='Inquiry',
        ),
    ]
