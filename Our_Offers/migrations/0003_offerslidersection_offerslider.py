# Generated by Django 5.1.3 on 2024-11-27 23:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Our_Offers', '0002_offercard_content_one_ar_offercard_content_one_en_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfferSliderSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_banner', models.ImageField(blank=True, help_text='Optional - you can upload an image or leave it blank. <br> If no image is selected, a default image will be displayed.', null=True, upload_to='Our_Services/Body_work_And_Painting/image_banner/', verbose_name='Image Banner')),
                ('title', models.CharField(blank=True, help_text='Maximum characters 50', max_length=50, null=True, verbose_name='title')),
                ('title_ar', models.CharField(blank=True, help_text='Maximum characters 50', max_length=50, null=True, verbose_name='title')),
                ('title_en', models.CharField(blank=True, help_text='Maximum characters 50', max_length=50, null=True, verbose_name='title')),
                ('description', models.TextField(blank=True, help_text='Maximum characters 1000', max_length=1000, null=True, verbose_name='Description')),
                ('description_ar', models.TextField(blank=True, help_text='Maximum characters 1000', max_length=1000, null=True, verbose_name='Description')),
                ('description_en', models.TextField(blank=True, help_text='Maximum characters 1000', max_length=1000, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'offer Slider',
                'verbose_name_plural': ' offer  Selider',
            },
        ),
        migrations.CreateModel(
            name='OfferSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='work_card/icons/', verbose_name='image')),
                ('slider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offer_sliders', to='Our_Offers.offerslidersection')),
            ],
            options={
                'verbose_name': 'offer Selider',
                'verbose_name_plural': 'offer Selider',
            },
        ),
    ]
