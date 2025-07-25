# Generated by Django 5.2.4 on 2025-07-18 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChaiBarity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='chais/')),
                ('type', models.CharField(choices=[('DP', 'DOODPATI_CHAI'), ('G', 'GHOR_CHAI'), ('KI', 'KASHMIRY_CHAI'), ('NR', 'NORMAL_CHAI'), ('SL', 'SULIMANI_CHAI')], max_length=2)),
            ],
        ),
    ]
