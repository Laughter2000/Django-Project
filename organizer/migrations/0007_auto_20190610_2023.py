# Generated by Django 2.2 on 2019-06-11 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0006_newslink_unique_together_slug_startup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startup',
            name='tags',
            field=models.ManyToManyField(blank=True, to='organizer.Tag'),
        ),
    ]
