# Generated by Django 2.1.2 on 2018-10-12 20:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0005_module_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='module_comment',
            name='date_posted',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='module_comment',
            name='content',
            field=models.TextField(max_length=500),
        ),
    ]
