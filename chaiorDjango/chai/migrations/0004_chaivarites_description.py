# Generated by Django 5.2.4 on 2025-07-20 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chai', '0003_chaivarites_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='chaivarites',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
