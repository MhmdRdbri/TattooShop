# Generated by Django 4.2.4 on 2023-09-30 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pattern', '0015_alter_tags_options_pattern_cover_pattern_duration_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PatternImage',
        ),
    ]