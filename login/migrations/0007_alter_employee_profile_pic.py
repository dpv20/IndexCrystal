# Generated by Django 4.2.5 on 2023-12-06 13:48

from django.db import migrations, models
import login.models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_alter_employee_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=login.models.get_profile_pic_filename),
        ),
    ]
