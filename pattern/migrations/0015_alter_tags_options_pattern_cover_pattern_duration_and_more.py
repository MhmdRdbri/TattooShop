# Generated by Django 4.2.4 on 2023-09-30 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pattern', '0014_alter_pattern_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tags',
            options={},
        ),
        migrations.AddField(
            model_name='pattern',
            name='cover',
            field=models.FileField(default=models.ImageField(upload_to='images/patterns/'), upload_to='images/cover/patterns/'),
        ),
        migrations.AddField(
            model_name='pattern',
            name='duration',
            field=models.CharField(default='Type...', max_length=200),
        ),
        migrations.AddField(
            model_name='tags',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='tags',
            name='follow_nofollow',
            field=models.CharField(blank=True, choices=[('follow', 'follow'), ('nofollow', 'nofollow')], default='follow', max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='tags',
            name='index_noindex',
            field=models.CharField(blank=True, choices=[('index', 'index'), ('noindex', 'noindex')], default='index', max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='tags',
            name='twitter_description',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Twitter:description'),
        ),
        migrations.AddField(
            model_name='tags',
            name='twitter_title',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Twitter:title'),
        ),
        migrations.AlterField(
            model_name='pattern',
            name='image',
            field=models.ImageField(upload_to='images/patterns/'),
        ),
        migrations.AlterField(
            model_name='pattern',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos/patterns/'),
        ),
        migrations.AlterField(
            model_name='tags',
            name='extratag',
            field=models.TextField(blank=True, null=True, verbose_name='تگ های جدید'),
        ),
        migrations.AlterField(
            model_name='tags',
            name='schema1',
            field=models.TextField(blank=True, null=True, verbose_name='اسکیما'),
        ),
        migrations.AlterField(
            model_name='tags',
            name='schema2',
            field=models.TextField(blank=True, null=True, verbose_name='اسکیما'),
        ),
    ]
