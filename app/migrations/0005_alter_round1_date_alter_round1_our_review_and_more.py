# Generated by Django 4.1.7 on 2023-07-13 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_project_edited_by_round1_edited_by_round2_edited_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='round1',
            name='date',
            field=models.DateField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='round1',
            name='our_review',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='round2',
            name='client_review',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='round2',
            name='date',
            field=models.DateField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='round2',
            name='our_review',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='round3',
            name='client_review',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='round3',
            name='date',
            field=models.DateField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='round3',
            name='our_review',
            field=models.TextField(blank=True, default=''),
        ),
    ]