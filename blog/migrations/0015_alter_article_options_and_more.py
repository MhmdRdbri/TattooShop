# Generated by Django 4.2.4 on 2023-09-12 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_alter_article_pub_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('-created_at',), 'verbose_name': 'مقاله', 'verbose_name_plural': 'مقاله ها'},
        ),
        migrations.RenameField(
            model_name='article',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='updated',
            new_name='updated_at',
        ),
        migrations.RemoveField(
            model_name='article',
            name='pub_date',
        ),
    ]