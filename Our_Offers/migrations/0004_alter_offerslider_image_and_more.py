# Generated by Django 5.1.3 on 2024-12-02 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Our_Offers', '0003_offerslidersection_offerslider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offerslider',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='OfferSliderSection/icons/', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='offerslidersection',
            name='image_banner',
            field=models.ImageField(blank=True, help_text='Optional - you can upload an image or leave it blank. <br> If no image is selected, a default image will be displayed.', null=True, upload_to='OfferSliderSection/image_banner/', verbose_name='Image Banner'),
        ),
    ]