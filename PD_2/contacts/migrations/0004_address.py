# Generated by Django 2.2.7 on 2019-12-03 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_phonenumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(blank=True, choices=[('work', 'work'), ('home', 'home'), ('other', 'other'), (None, None)], default=None, max_length=30, null=True, verbose_name="Address's role")),
                ('street', models.CharField(max_length=30, verbose_name='Street')),
                ('number', models.CharField(max_length=60, verbose_name='Street number')),
                ('flat_number', models.PositiveIntegerField(blank=True, default=None, null=True, verbose_name='flat_number')),
                ('postal_code', models.CharField(max_length=10, verbose_name='Postal code')),
                ('city', models.CharField(max_length=60, verbose_name='City')),
                ('country', models.CharField(max_length=60, verbose_name='Country')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.Person')),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addresses',
            },
        ),
    ]
