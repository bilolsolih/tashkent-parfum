# Generated by Django 4.2.1 on 2023-05-18 09:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0006_alter_user_is_active"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(
                default=False,
                help_text="Designates whether this user should be treated as active.Unselect this instead of deleting accounts.",
                verbose_name="Is active?",
            ),
        ),
    ]
