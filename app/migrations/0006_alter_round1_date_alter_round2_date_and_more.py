# Generated by Django 4.1.7 on 2023-07-13 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_round1_date_alter_round1_our_review_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='round1',
            name='date',
            field=models.DateField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='round2',
            name='date',
            field=models.DateField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='round3',
            name='date',
            field=models.DateField(blank=True, default='', null=True),
        ),
    ]
