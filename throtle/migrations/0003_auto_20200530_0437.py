# Generated by Django 3.0.4 on 2020-05-29 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('throtle', '0002_auto_20200530_0432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityperiod',
            name='pid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_periods', to='throtle.User'),
        ),
    ]