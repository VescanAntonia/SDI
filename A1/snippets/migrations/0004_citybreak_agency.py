# Generated by Django 4.1.7 on 2023-03-16 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0003_citybreak_citybreakperson_person_travelagency_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='citybreak',
            name='agency',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='snippets.travelagency'),
        ),
    ]
