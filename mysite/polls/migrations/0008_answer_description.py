# Generated by Django 2.0.5 on 2018-09-05 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20180905_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='description',
            field=models.TextField(blank=True, help_text='a description of the answer', verbose_name='Description'),
        ),
    ]