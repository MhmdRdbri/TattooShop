# Generated by Django 4.2.4 on 2023-09-14 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pattern', '0002_pattern_canonical_pattern_descriptionog_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatternCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
            ],
        ),
        migrations.CreateModel(
            name='PatternImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pattern_images/')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('pattern', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='pattern.pattern')),
            ],
        ),
        migrations.AddField(
            model_name='pattern',
            name='category',
            field=models.ManyToManyField(related_name='articles', to='pattern.patterncategory', verbose_name='Category'),
        ),
    ]
