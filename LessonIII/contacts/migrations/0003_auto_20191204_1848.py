# Generated by Django 2.2.7 on 2019-12-04 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_address_email_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='friends',
            field=models.ManyToManyField(blank=True, default=None, to='contacts.Person', verbose_name='Friends'),
        ),
    ]
