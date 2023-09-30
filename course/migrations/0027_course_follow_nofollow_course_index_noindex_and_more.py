# Generated by Django 4.2.4 on 2023-09-30 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0026_alter_course_schema1'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='follow_nofollow',
            field=models.CharField(choices=[('follow', 'follow'), ('nofollow', 'nofollow')], default='follow', max_length=150),
        ),
        migrations.AddField(
            model_name='course',
            name='index_noindex',
            field=models.CharField(choices=[('index', 'index'), ('noindex', 'noindex')], default='index', max_length=150),
        ),
        migrations.AddField(
            model_name='course',
            name='twitter_description',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Twitter:description'),
        ),
        migrations.AddField(
            model_name='course',
            name='twitter_title',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Twitter:title'),
        ),
        migrations.AddField(
            model_name='pagetags',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='pagetags',
            name='follow_nofollow',
            field=models.CharField(choices=[('follow', 'follow'), ('nofollow', 'nofollow')], default='follow', max_length=150),
        ),
        migrations.AddField(
            model_name='pagetags',
            name='index_noindex',
            field=models.CharField(choices=[('index', 'index'), ('noindex', 'noindex')], default='index', max_length=150),
        ),
        migrations.AddField(
            model_name='pagetags',
            name='twitter_description',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Twitter:description'),
        ),
        migrations.AddField(
            model_name='pagetags',
            name='twitter_title',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Twitter:title'),
        ),
        migrations.AddField(
            model_name='tags',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='tags',
            name='follow_nofollow',
            field=models.CharField(choices=[('follow', 'follow'), ('nofollow', 'nofollow')], default='follow', max_length=150),
        ),
        migrations.AddField(
            model_name='tags',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/Tags', verbose_name='تصویر'),
        ),
        migrations.AddField(
            model_name='tags',
            name='index_noindex',
            field=models.CharField(choices=[('index', 'index'), ('noindex', 'noindex')], default='index', max_length=150),
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
            model_name='course',
            name='extratag',
            field=models.TextField(blank=True, null=True, verbose_name='تگ های جدید'),
        ),
        migrations.AlterField(
            model_name='course',
            name='schema1',
            field=models.TextField(blank=True, null=True, verbose_name='اسکیما'),
        ),
        migrations.AlterField(
            model_name='course',
            name='schema2',
            field=models.TextField(blank=True, null=True, verbose_name='اسکیما'),
        ),
        migrations.AlterField(
            model_name='pagetags',
            name='extratag',
            field=models.TextField(blank=True, null=True, verbose_name='تگ های جدید'),
        ),
        migrations.AlterField(
            model_name='pagetags',
            name='schema1',
            field=models.TextField(blank=True, null=True, verbose_name='اسکیما'),
        ),
        migrations.AlterField(
            model_name='pagetags',
            name='schema2',
            field=models.TextField(blank=True, null=True, verbose_name='اسکیما'),
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