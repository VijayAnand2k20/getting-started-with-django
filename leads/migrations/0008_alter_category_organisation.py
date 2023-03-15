# Generated by Django 4.1.7 on 2023-03-11 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("leads", "0007_category_organisation"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="organisation",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="leads.userprofile"
            ),
        ),
    ]
