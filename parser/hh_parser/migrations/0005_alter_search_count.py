# Generated by Django 5.0.7 on 2024-07-31 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hh_parser', '0004_alter_requirements_skill_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='count',
            field=models.IntegerField(),
        ),
    ]