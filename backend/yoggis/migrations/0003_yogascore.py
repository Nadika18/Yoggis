# Generated by Django 4.1.5 on 2023-01-11 16:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('yoggis', '0002_userdisorder_yogacategory_yoga_lower_age_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='YogaScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
