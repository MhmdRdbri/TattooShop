# Generated by Django 4.2.4 on 2023-09-23 18:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0013_rename_article_comment_course'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ('-created_at',), 'verbose_name': 'دوره', 'verbose_name_plural': 'دوره ها'},
        ),
    ]