# Generated by Django 5.1.7 on 2025-04-15 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(upload_to='projects/'),
        ),
        migrations.CreateModel(
            name='PortfolioInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('job_position', models.CharField(max_length=100)),
                ('degree_name', models.CharField(max_length=100)),
                ('avatar', models.ImageField(upload_to='avatars/')),
                ('about_me', models.TextField()),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('github', models.URLField()),
                ('linkedin', models.URLField()),
                ('projects', models.ManyToManyField(to='portfolio.project')),
            ],
        ),
    ]
