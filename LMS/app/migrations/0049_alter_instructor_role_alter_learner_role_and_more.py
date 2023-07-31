# Generated by Django 4.1.6 on 2023-06-05 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0048_alter_instructor_role_alter_learner_role_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="instructor",
            name="role",
            field=models.ForeignKey(
                default="Instructor",
                on_delete=django.db.models.deletion.CASCADE,
                to="app.role",
            ),
        ),
        migrations.AlterField(
            model_name="learner",
            name="role",
            field=models.ForeignKey(
                default="Learner",
                on_delete=django.db.models.deletion.CASCADE,
                to="app.role",
            ),
        ),
        migrations.AlterField(
            model_name="role",
            name="role",
            field=models.CharField(
                choices=[("Learner", "Learner"), ("Instructor", "Instructor")],
                max_length=10,
            ),
        ),
    ]
