# Generated by Django 3.1.2 on 2021-02-12 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserRegisterApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registereduser',
            name='contact_number',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='registereduser',
            name='country_of_residence',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='registereduser',
            name='middle_name',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='registereduser',
            name='willingness_to_join_session',
            field=models.CharField(blank=True, choices=[('YES', 'Yes'), ('NO', 'No'), ('MAYBE', 'May be')], max_length=10),
        ),
    ]