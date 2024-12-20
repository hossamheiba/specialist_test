# Generated by Django 5.1.3 on 2024-11-27 23:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, help_text='Maximum characters 50', max_length=50, null=True, verbose_name='title')),
                ('title_ar', models.CharField(blank=True, help_text='Maximum characters 50', max_length=50, null=True, verbose_name='title')),
                ('title_en', models.CharField(blank=True, help_text='Maximum characters 50', max_length=50, null=True, verbose_name='title')),
            ],
            options={
                'verbose_name': 'news Section',
                'verbose_name_plural': ' news Sections',
            },
        ),
        migrations.CreateModel(
            name='NewsSliderSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_banner', models.ImageField(blank=True, help_text='Optional - you can upload an image or leave it blank. <br> If no image is selected, a default image will be displayed.', null=True, upload_to='Our_Services/Body_work_And_Painting/image_banner/', verbose_name='Image Banner')),
                ('title', models.CharField(blank=True, help_text='Maximum characters 50', max_length=50, null=True, verbose_name='title')),
                ('title_ar', models.CharField(blank=True, help_text='Maximum characters 50', max_length=50, null=True, verbose_name='title')),
                ('title_en', models.CharField(blank=True, help_text='Maximum characters 50', max_length=50, null=True, verbose_name='title')),
            ],
            options={
                'verbose_name': 'news Slider',
                'verbose_name_plural': ' news  Selider',
            },
        ),
        migrations.CreateModel(
            name='NewsCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background_card', models.ImageField(blank=True, null=True, upload_to='work_card/icons/', verbose_name='background_card')),
                ('title', models.CharField(blank=True, help_text='Maximum characters 30', max_length=30, null=True, verbose_name='title')),
                ('title_ar', models.CharField(blank=True, help_text='Maximum characters 30', max_length=30, null=True, verbose_name='title')),
                ('title_en', models.CharField(blank=True, help_text='Maximum characters 30', max_length=30, null=True, verbose_name='title')),
                ('content', models.CharField(blank=True, help_text='Maximum characters 100', max_length=100, null=True, verbose_name='content')),
                ('content_ar', models.CharField(blank=True, help_text='Maximum characters 100', max_length=100, null=True, verbose_name='content')),
                ('content_en', models.CharField(blank=True, help_text='Maximum characters 100', max_length=100, null=True, verbose_name='content')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_cards', to='Media_Center.newssection')),
            ],
            options={
                'verbose_name': 'news Card',
                'verbose_name_plural': 'news Cards',
            },
        ),
        migrations.CreateModel(
            name='NewsSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='work_card/icons/', verbose_name='image')),
                ('slider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_sliders', to='Media_Center.newsslidersection')),
            ],
            options={
                'verbose_name': 'news Selider',
                'verbose_name_plural': 'news Selider',
            },
        ),
    ]
