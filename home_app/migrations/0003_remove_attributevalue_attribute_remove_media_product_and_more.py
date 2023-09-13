# Generated by Django 4.2.4 on 2023-09-12 11:09

from django.db import migrations, models
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0002_attribute_attributevalue_productattribute'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attributevalue',
            name='attribute',
        ),
        migrations.RemoveField(
            model_name='media',
            name='product',
        ),
        migrations.RemoveField(
            model_name='productattribute',
            name='attribute_value',
        ),
        migrations.RemoveField(
            model_name='productattribute',
            name='product',
        ),
        migrations.RemoveField(
            model_name='pattern',
            name='images_and_videos',
        ),
        migrations.AddField(
            model_name='pattern',
            name='alt',
            field=models.CharField(default='Alt', max_length=100, verbose_name='Alt'),
        ),
        migrations.AlterField(
            model_name='pattern',
            name='description',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='Text'),
        ),
        migrations.DeleteModel(
            name='Attribute',
        ),
        migrations.DeleteModel(
            name='AttributeValue',
        ),
        migrations.DeleteModel(
            name='Media',
        ),
        migrations.DeleteModel(
            name='ProductAttribute',
        ),
    ]