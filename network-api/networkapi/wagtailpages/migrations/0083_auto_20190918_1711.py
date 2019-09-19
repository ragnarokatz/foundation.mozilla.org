# Generated by Django 2.2.4 on 2019-09-18 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailpages', '0082_homepagefeaturedblogs'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='author_de',
            field=models.CharField(max_length=70, null=True, verbose_name='Author'),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='author_en',
            field=models.CharField(max_length=70, null=True, verbose_name='Author'),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='author_es',
            field=models.CharField(max_length=70, null=True, verbose_name='Author'),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='author_fr',
            field=models.CharField(max_length=70, null=True, verbose_name='Author'),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='author_pl',
            field=models.CharField(max_length=70, null=True, verbose_name='Author'),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='author_pt',
            field=models.CharField(max_length=70, null=True, verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='author',
            field=models.CharField(max_length=70, verbose_name='Author'),
        ),
    ]
