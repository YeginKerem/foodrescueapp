# Generated by Django 4.2 on 2024-12-31 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodrescue', '0003_deleteddonationlogs_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deleteddonationlogs',
            name='description',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
