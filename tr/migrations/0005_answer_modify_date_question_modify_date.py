# Generated by Django 4.0.1 on 2022-01-28 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tr', '0004_alter_answer_author_alter_question_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]