# Generated by Django 3.2.6 on 2021-10-16 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('routine', '0003_targetaudience'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='target_audience',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='routine.targetaudience'),
            preserve_default=False,
        ),
    ]
