# Generated by Django 4.1.3 on 2022-11-30 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("task", "0002_rename_teg_tag_rename_teg_task_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="tags",
            field=models.ManyToManyField(to="task.tag"),
        ),
    ]
