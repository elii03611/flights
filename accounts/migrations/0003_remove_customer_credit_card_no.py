# Generated by Django 4.2.1 on 2023-05-20 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_adminstrator_user_roles_delete_user_role_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='credit_card_no',
        ),
    ]