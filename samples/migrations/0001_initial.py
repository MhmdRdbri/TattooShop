# Generated by Django 4.2.4 on 2023-09-15 08:38

from django.db import migrations, models
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Samples',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('title', models.CharField(max_length=250)),
                ('author', models.CharField(choices=[('Z', 'ضیائی'), ('K', 'کارآموز')], default='Z', max_length=1)),
                ('description', django_ckeditor_5.fields.CKEditor5Field(verbose_name='Text')),
                ('video', models.FileField(upload_to='video/samples')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]