# Generated by Django 4.1.6 on 2023-06-04 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0045_alter_instructor_role_alter_learner_role"),
    ]

    operations = [
        migrations.AlterField(
            model_name="role",
            name="role",
            field=models.CharField(
                choices=[("0", "Learner"), ("1", "Instructor")], max_length=10
            ),
        ),
    ]