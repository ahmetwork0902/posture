# Generated by Django 4.2.7 on 2023-12-05 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osanka', '0003_achievements_sessions_remove_users_date_from_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='phone_number',
            field=models.CharField(max_length=11, null=True),
        ),
    ]
