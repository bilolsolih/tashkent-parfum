# Generated by Django 4.2.1 on 2023-05-18 09:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("verification", "0003_remove_verificationcode_full_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="verificationcode",
            name="full_name",
            field=models.CharField(default="banzaaaaay", max_length=128),
            preserve_default=False,
        ),
    ]
