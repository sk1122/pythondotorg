# Generated by Django 2.0.13 on 2020-10-14 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("sponsors", "0003_auto_20170821_2000"),
    ]

    operations = [
        migrations.CreateModel(
            name="SponsorshipBenefit",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "order",
                    models.PositiveIntegerField(
                        db_index=True, editable=False, verbose_name="order"
                    ),
                ),
                ("name", models.CharField(max_length=64)),
                ("description", models.TextField(blank=True, null=True)),
                ("value", models.PositiveIntegerField(blank=True, null=True)),
                (
                    "conflicts",
                    models.ManyToManyField(
                        related_name="_sponsorshipbenefit_conflicts_+",
                        to="sponsors.SponsorshipBenefit",
                    ),
                ),
            ],
            options={
                "ordering": ("order",),
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="SponsorshipLevel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "order",
                    models.PositiveIntegerField(
                        db_index=True, editable=False, verbose_name="order"
                    ),
                ),
                ("name", models.CharField(max_length=64)),
                ("sponsorship_amount", models.PositiveIntegerField()),
            ],
            options={
                "ordering": ("order",),
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="SponsorshipProgram",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "order",
                    models.PositiveIntegerField(
                        db_index=True, editable=False, verbose_name="order"
                    ),
                ),
                ("name", models.CharField(max_length=64)),
                ("description", models.TextField(blank=True, null=True)),
            ],
            options={
                "ordering": ("order",),
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="sponsorshipbenefit",
            name="levels",
            field=models.ManyToManyField(
                related_name="benefits", to="sponsors.SponsorshipLevel"
            ),
        ),
        migrations.AddField(
            model_name="sponsorshipbenefit",
            name="minimum_level",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="sponsors.SponsorshipLevel",
            ),
        ),
        migrations.AddField(
            model_name="sponsorshipbenefit",
            name="program",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="sponsors.SponsorshipProgram",
            ),
        ),
    ]
