# Generated by Django 2.0.1 on 2018-02-05 00:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_auto_20180205_0012'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='content',
            new_name='contact_content',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='email',
            new_name='contact_email',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='name',
            new_name='contact_name',
        ),
    ]
