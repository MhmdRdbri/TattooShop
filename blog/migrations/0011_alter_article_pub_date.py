# Generated by Django 4.2.4 on 2023-09-11 20:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_article_view_count_alter_article_pub_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2023, 9, 11, 23, 50, 10, 87300), verbose_name='Publish Date'),
        ),
    ]