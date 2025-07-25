# Generated by Django 5.2.4 on 2025-07-18 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chai', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChaiVarites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='chais/')),
                ('type', models.CharField(choices=[('DP', 'Doodhpati Chai'), ('G', 'Ghor Chai'), ('KI', 'Kashmiri Chai'), ('NR', 'Normal Chai'), ('SL', 'Sulemani Chai')], max_length=2)),
            ],
        ),
        migrations.DeleteModel(
            name='ChaiBarity',
        ),
    ]
