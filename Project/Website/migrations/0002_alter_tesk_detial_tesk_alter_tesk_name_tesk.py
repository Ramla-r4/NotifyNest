# Generated by Django 4.2.8 on 2024-05-28 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tesk',
            name='Detial_tesk',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='tesk',
            name='Name_tesk',
            field=models.CharField(max_length=100),
        ),
    ]
