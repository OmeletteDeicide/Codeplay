# Generated by Django 5.0.7 on 2024-07-26 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_exercise_expected_output_exercise_test_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='expected_output',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='test_code',
            field=models.TextField(default=''),
        ),
    ]
