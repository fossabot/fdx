# Generated by Django 2.2.4 on 2019-08-20 21:34

import any_imagefield.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fdx_search', '0002_auto_20190819_2037'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', any_imagefield.models.fields.AnyImageField(upload_to='searches', verbose_name='Image')),
                ('face_count', models.IntegerField(blank=True, default=0, verbose_name='Face Count')),
            ],
            options={
                'verbose_name': 'Картинки загруженные для поиска',
                'verbose_name_plural': 'Картинки загруженные для поиска',
            },
        ),
        migrations.AlterField(
            model_name='faces',
            name='bottom',
            field=models.IntegerField(blank=True, default=0, verbose_name='Bottom'),
        ),
        migrations.AlterField(
            model_name='faces',
            name='left',
            field=models.IntegerField(blank=True, default=0, verbose_name='Left'),
        ),
        migrations.AlterField(
            model_name='faces',
            name='right',
            field=models.IntegerField(blank=True, default=0, verbose_name='Right'),
        ),
        migrations.AlterField(
            model_name='faces',
            name='top',
            field=models.IntegerField(blank=True, default=0, verbose_name='Top'),
        ),
    ]
