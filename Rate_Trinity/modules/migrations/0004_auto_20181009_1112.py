# Generated by Django 2.1.2 on 2018-10-09 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0003_auto_20181008_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='lecturer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='lecturers.Lecturer'),
        ),
    ]
