# Generated by Django 4.2.1 on 2023-05-25 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module001', '0008_tests_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.CharField(max_length=254, null=True)),
                ('correctanswer', models.CharField(max_length=254, null=True)),
            ],
            options={
                'verbose_name_plural': 'Answers',
            },
        ),
    ]