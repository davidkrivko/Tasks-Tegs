# Generated by Django 4.1.3 on 2022-11-30 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("task", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Teg",
            new_name="Tag",
        ),
        migrations.RenameField(
            model_name="task",
            old_name="teg",
            new_name="tags",
        ),
    ]
