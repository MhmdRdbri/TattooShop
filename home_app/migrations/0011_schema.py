# Generated by Django 4.2.4 on 2023-09-27 08:26

from django.db import migrations, models
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0010_alter_extratags_field'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schema1', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='اسکیما')),
                ('schema2', django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True, verbose_name='اسکیما')),
            ],
        ),
    ]
