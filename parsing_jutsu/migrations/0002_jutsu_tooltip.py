# Generated by Django 5.1.3 on 2024-11-28 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsing_jutsu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jutsu',
            name='tooltip',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
