# Generated by Django 4.2.4 on 2023-09-27 08:09

from django.db import migrations
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_alter_article_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='tags',
            name='extratag',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='متن'),
        ),
    ]
