# Generated by Django 4.2.8 on 2024-09-23 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0004_rename_reminder_time_tesk_due_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tesk',
            name='user_email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]
