# Generated by Django 4.1.7 on 2023-07-13 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_round1_date_alter_round2_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bde_user',
            name='username',
            field=models.CharField(max_length=256, unique=True),
        ),
    ]