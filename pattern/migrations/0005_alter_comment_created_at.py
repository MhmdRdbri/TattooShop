# Generated by Django 4.2.4 on 2023-09-14 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pattern', '0004_alter_pattern_created_at_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created'),
        ),
    ]
