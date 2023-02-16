# Generated by Django 4.1.7 on 2023-02-14 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cafe',
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
                ("name", models.CharField(max_length=32)),
                ("address", models.CharField(max_length=128)),
                ("image", models.ImageField(upload_to="cafephoto/")),
                ("runtime", models.CharField(max_length=48)),
                ("menu", models.TextField()),
                ("number", models.CharField(max_length=16)),
                ("latitude", models.FloatField(default=37.314964)),
                ("longtitude", models.FloatField(default=126.575308)),
                ("keywords",models.TextField(null=True))
                ('average_star', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CafeKeyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword_list', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
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
                ("name", models.CharField(max_length=32)),
               
            ],
        ),
        migrations.CreateModel(
            name='CafeLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cafe_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cafe_like', to='Cafe.cafe')),
            ],
        ),
    ]
