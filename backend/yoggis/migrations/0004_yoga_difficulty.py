# Generated by Django 4.1.5 on 2023-01-11 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yoggis', '0003_yogascore'),
    ]

    operations = [
        migrations.AddField(
            model_name='yoga',
            name='difficulty',
            field=models.CharField(choices=[('C', 'Beginner'), ('B', 'Intermediate'), ('A', 'Advanced Intermediate'), ('S', 'Expert')], default='C', max_length=1),
        ),
    ]
