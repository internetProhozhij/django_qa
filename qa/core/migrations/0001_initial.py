# Generated by Django 4.2 on 2023-06-09 10:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionModel',
            fields=[
                ('qid', models.CharField(max_length=256, primary_key=True, serialize=False)),
                ('theme', models.CharField(choices=[('prog', 'Программирование'), ('admin', 'Администрирование'), ('other', 'Другое'), ('music', 'Музыка'), ('movie', 'Кино'), ('serial', 'Сериалы'), ('anime', 'Аниме')], max_length=256)),
                ('date', models.DateTimeField(auto_now=True)),
                ('header', models.CharField(max_length=140)),
                ('body', models.TextField()),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AnswerModel',
            fields=[
                ('aid', models.CharField(max_length=256, primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now=True)),
                ('body', models.TextField()),
                ('qid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.questionmodel')),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
