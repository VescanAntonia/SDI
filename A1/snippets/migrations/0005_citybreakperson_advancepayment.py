# Generated by Django 4.1.7 on 2023-03-17 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0004_citybreak_agency'),
    ]

    operations = [
        migrations.AddField(
            model_name='citybreakperson',
            name='advancePayment',
            field=models.FloatField(default=50),
        ),
    ]