# Generated by Django 5.1.3 on 2024-11-22 20:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Our_Services', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mechanics',
            options={'verbose_name': 'Mechanic', 'verbose_name_plural': 'Mechanics'},
        ),
        migrations.RemoveField(
            model_name='mechanics',
            name='description_first_section',
        ),
        migrations.RemoveField(
            model_name='mechanics',
            name='image_first_section',
        ),
        migrations.RemoveField(
            model_name='mechanics',
            name='title_first_section',
        ),
        migrations.AddField(
            model_name='mechanics',
            name='first_section_description',
            field=models.TextField(blank=True, help_text='Description of the first section', null=True, verbose_name='First Section Description'),
        ),
        migrations.AddField(
            model_name='mechanics',
            name='first_section_description_ar',
            field=models.TextField(blank=True, help_text='Description of the first section', null=True, verbose_name='First Section Description'),
        ),
        migrations.AddField(
            model_name='mechanics',
            name='first_section_description_en',
            field=models.TextField(blank=True, help_text='Description of the first section', null=True, verbose_name='First Section Description'),
        ),
        migrations.AddField(
            model_name='mechanics',
            name='first_section_image',
            field=models.ImageField(blank=True, help_text='Optional - recommended to use an image with a transparent background.', null=True, upload_to='mechanics/first_section/', verbose_name='First Section Image'),
        ),
        migrations.AddField(
            model_name='mechanics',
            name='first_section_title',
            field=models.CharField(blank=True, help_text='Maximum 50 characters', max_length=50, null=True, verbose_name='First Section Title'),
        ),
        migrations.AddField(
            model_name='mechanics',
            name='second_section_description',
            field=models.TextField(blank=True, help_text='Description of the second section', null=True, verbose_name='Second Section Description'),
        ),
        migrations.AddField(
            model_name='mechanics',
            name='second_section_description_ar',
            field=models.TextField(blank=True, help_text='Description of the second section', null=True, verbose_name='Second Section Description'),
        ),
        migrations.AddField(
            model_name='mechanics',
            name='second_section_description_en',
            field=models.TextField(blank=True, help_text='Description of the second section', null=True, verbose_name='Second Section Description'),
        ),
        migrations.AddField(
            model_name='mechanics',
            name='second_section_image',
            field=models.ImageField(blank=True, help_text='Optional - recommended to use an image with a transparent background.', null=True, upload_to='mechanics/second_section/', verbose_name='Second Section Image'),
        ),
        migrations.AddField(
            model_name='mechanics',
            name='second_section_title',
            field=models.CharField(blank=True, help_text='Maximum 50 characters', max_length=50, null=True, verbose_name='Second Section Title'),
        ),
        migrations.AddField(
            model_name='mechanics',
            name='second_section_title_ar',
            field=models.CharField(blank=True, help_text='Maximum 50 characters', max_length=50, null=True, verbose_name='Second Section Title'),
        ),
        migrations.AddField(
            model_name='mechanics',
            name='second_section_title_en',
            field=models.CharField(blank=True, help_text='Maximum 50 characters', max_length=50, null=True, verbose_name='Second Section Title'),
        ),
        migrations.AlterField(
            model_name='mechanics',
            name='image_banner',
            field=models.ImageField(blank=True, help_text='Optional - you can upload an image or leave it blank. <br> If no image is selected, a default image will be displayed.', null=True, upload_to='mechanics/image_banner/', verbose_name='Image Banner'),
        ),
        migrations.CreateModel(
            name='MechanicSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider_image', models.ImageField(blank=True, help_text='Optional - you can upload an image or leave it blank. <br> If no image is selected, a default image will be displayed.', null=True, upload_to='mechanics/slider_images/', verbose_name='Slider Image')),
                ('mechanics', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sliders', to='Our_Services.mechanics', verbose_name='Mechanic')),
            ],
            options={
                'verbose_name': 'Mechanic Slider',
                'verbose_name_plural': 'Mechanic Sliders',
            },
        ),
    ]