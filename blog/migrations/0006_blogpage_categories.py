# Generated by Django 4.0.5 on 2022-06-17 08:10

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blogcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='categories',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='blog.blogcategory'),
        ),
    ]
