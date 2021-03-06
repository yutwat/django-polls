# Generated by Django 2.1.1 on 2018-09-25 11:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0011_auto_20180925_0914'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solution_text', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, help_text='a description of the answer', verbose_name='Description')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='answer',
            name='author',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.AddField(
            model_name='question',
            name='release_date',
            field=models.DateTimeField(null=True, verbose_name='release date'),
        ),
        migrations.AddField(
            model_name='question',
            name='release_flag',
            field=models.BooleanField(default=False, help_text='release or not'),
        ),
        migrations.AddField(
            model_name='question',
            name='week_num',
            field=models.CharField(default='week0', help_text='week number', max_length=50, verbose_name='week'),
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.AddField(
            model_name='solution',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Question'),
        ),
    ]
