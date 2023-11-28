# Generated by Django 4.2.7 on 2023-11-28 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="NewsArticle",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("content", models.TextField()),
                ("category", models.CharField(max_length=50)),
                ("cluster_label", models.IntegerField()),
                ("source_rating", models.FloatField(default=0.0)),
                ("pub_date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
