# Generated by Django 4.2.1 on 2023-05-23 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module001', '0003_alter_pages_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='pages',
            name='user',
            field=models.CharField(max_length=254, null=True),
        ),
    ]
