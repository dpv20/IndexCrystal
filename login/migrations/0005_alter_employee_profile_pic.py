# Generated by Django 4.2.5 on 2023-12-06 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_delete_customuser_employee_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='media/profile_pics/'),
        ),
    ]