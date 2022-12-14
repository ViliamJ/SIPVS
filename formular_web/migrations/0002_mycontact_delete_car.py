# Generated by Django 4.1.1 on 2022-09-28 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formular_web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(blank=True, max_length=50, null=True)),
                ('contact_group', models.CharField(blank=True, choices=[('PRE-SALES', 'PRE-SALES'), ('SALES', 'SALES'), ('SERVICE', 'SERVICE')], max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Car',
        ),
    ]
