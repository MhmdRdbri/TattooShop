# Generated by Django 4.2.4 on 2023-09-30 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0027_course_follow_nofollow_course_index_noindex_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagetags',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/Tags', verbose_name='تصویر'),
        ),
    ]
