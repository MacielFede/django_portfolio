# Generated by Django 5.1.7 on 2025-04-16 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_portfolioinfo_about_me_portfolioinfo_avatar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolioinfo',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='core/static/core/img/'),
        ),
    ]
