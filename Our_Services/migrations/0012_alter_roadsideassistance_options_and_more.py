# Generated by Django 5.1.3 on 2024-11-26 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Our_Services', '0011_roadsideassistance_roadsideassistanceslider'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='roadsideassistance',
            options={'verbose_name': 'roadsideassistance', 'verbose_name_plural': 'roadsideassistance'},
        ),
        migrations.AlterField(
            model_name='bodyworkandpainting',
            name='first_section_image',
            field=models.ImageField(blank=True, help_text='Optional - recommended to use an image with a transparent background.', null=True, upload_to='Our_Services/Body_work_And_Painting/first_section_image/', verbose_name='First Section Image'),
        ),
        migrations.AlterField(
            model_name='bodyworkandpainting',
            name='image_banner',
            field=models.ImageField(blank=True, help_text='Optional - you can upload an image or leave it blank. <br> If no image is selected, a default image will be displayed.', null=True, upload_to='Our_Services/Body_work_And_Painting/image_banner/', verbose_name='Image Banner'),
        ),
        migrations.AlterField(
            model_name='bodyworkandpainting',
            name='second_section_image',
            field=models.ImageField(blank=True, help_text='Optional - recommended to use an image with a transparent background.', null=True, upload_to='Our_Services/Body_work_And_Painting/second_section_image/', verbose_name='Second Section Image'),
        ),
        migrations.AlterField(
            model_name='bodyworkandpaintingslider',
            name='slider_image',
            field=models.ImageField(blank=True, help_text='Optional - you can upload an image or leave it blank. <br> If no image is selected, a default image will be displayed.', null=True, upload_to='Our_Services/Body_work_And_Painting/slider_image/', verbose_name='Slider Image'),
        ),
        migrations.AlterField(
            model_name='carprogramming',
            name='first_section_image',
            field=models.ImageField(blank=True, help_text='Optional - recommended to use an image with a transparent background.', null=True, upload_to='Our_Services/Car_Programming/first_section_image/', verbose_name='First Section Image'),
        ),
        migrations.AlterField(
            model_name='carprogramming',
            name='image_banner',
            field=models.ImageField(blank=True, help_text='Optional - you can upload an image or leave it blank. <br> If no image is selected, a default image will be displayed.', null=True, upload_to='Our_Services/Car_Programming/image_banner/', verbose_name='Image Banner'),
        ),
        migrations.AlterField(
            model_name='carprogramming',
            name='second_section_image',
            field=models.ImageField(blank=True, help_text='Optional - recommended to use an image with a transparent background.', null=True, upload_to='Our_Services/Car_Programming/second_section_image/', verbose_name='Second Section Image'),
        ),
        migrations.AlterField(
            model_name='carprogrammingslider',
            name='slider_image',
            field=models.ImageField(blank=True, help_text='Optional - you can upload an image or leave it blank. <br> If no image is selected, a default image will be displayed.', null=True, upload_to='Our_Services/Car_Programming/slider_image/', verbose_name='Slider Image'),
        ),
        migrations.AlterField(
            model_name='electricity',
            name='first_section_image',
            field=models.ImageField(blank=True, help_text='Optional - recommended to use an image with a transparent background.', null=True, upload_to='Our_Services/Electricity/first_section_image/', verbose_name='First Section Image'),
        ),
        migrations.AlterField(
            model_name='electricity',
            name='image_banner',
            field=models.ImageField(blank=True, help_text='Optional - you can upload an image or leave it blank. <br> If no image is selected, a default image will be displayed.', null=True, upload_to='Our_Services/Electricity/image_banner/', verbose_name='Image Banner'),
        ),
        migrations.AlterField(
            model_name='electricity',
            name='second_section_image',
            field=models.ImageField(blank=True, help_text='Optional - recommended to use an image with a transparent background.', null=True, upload_to='Our_Services/Electricity/second_section_image/', verbose_name='Second Section Image'),
        ),
        migrations.AlterField(
            model_name='electricityslider',
            name='slider_image',
            field=models.ImageField(blank=True, help_text='Optional - you can upload an image or leave it blank. <br> If no image is selected, a default image will be displayed.', null=True, upload_to='Our_Services/Electricity/slider_image/', verbose_name='Slider Image'),
        ),
        migrations.AlterField(
            model_name='mechanics',
            name='first_section_image',
            field=models.ImageField(blank=True, help_text='Optional - recommended to use an image with a transparent background.', null=True, upload_to='Our_Services/Mechanics/first_section_image/', verbose_name='First Section Image'),
        ),
        migrations.AlterField(
            model_name='mechanics',
            name='second_section_image',
            field=models.ImageField(blank=True, help_text='Optional - recommended to use an image with a transparent background.', null=True, upload_to='Our_Services/Mechanics/second_section_image/', verbose_name='Second Section Image'),
        ),
        migrations.AlterField(
            model_name='mechanicslider',
            name='slider_image',
            field=models.ImageField(blank=True, help_text='Optional - you can upload an image or leave it blank. <br> If no image is selected, a default image will be displayed.', null=True, upload_to='Our_Services/Mechanics/slider_image/', verbose_name='Slider Image'),
        ),
        migrations.AlterField(
            model_name='roadsideassistance',
            name='first_section_image',
            field=models.ImageField(blank=True, help_text='Optional - recommended to use an image with a transparent background.', null=True, upload_to='Our_Services/Roadside_Assistance/first_section_image/', verbose_name='First Section Image'),
        ),
        migrations.AlterField(
            model_name='roadsideassistance',
            name='image_banner',
            field=models.ImageField(blank=True, help_text='Optional - you can upload an image or leave it blank. <br> If no image is selected, a default image will be displayed.', null=True, upload_to='Our_Services/Roadside_Assistance/image_banner/', verbose_name='Image Banner'),
        ),
        migrations.AlterField(
            model_name='roadsideassistance',
            name='second_section_image',
            field=models.ImageField(blank=True, help_text='Optional - recommended to use an image with a transparent background.', null=True, upload_to='Our_Services/Roadside_Assistance/second_section_image/', verbose_name='Second Section Image'),
        ),
        migrations.AlterField(
            model_name='roadsideassistanceslider',
            name='slider_image',
            field=models.ImageField(blank=True, help_text='Optional - you can upload an image or leave it blank. <br> If no image is selected, a default image will be displayed.', null=True, upload_to='Our_Services/Roadside_Assistance/slider_image/', verbose_name='Slider Image'),
        ),
        migrations.AlterField(
            model_name='sportssuspension',
            name='first_section_image',
            field=models.ImageField(blank=True, help_text='Optional - recommended to use an image with a transparent background.', null=True, upload_to='Our_Services/Car_Programming/first_section_image/', verbose_name='First Section Image'),
        ),
        migrations.AlterField(
            model_name='sportssuspension',
            name='image_banner',
            field=models.ImageField(blank=True, help_text='Optional - you can upload an image or leave it blank. <br> If no image is selected, a default image will be displayed.', null=True, upload_to='Our_Services/Sports_Suspension/image_banner/', verbose_name='Image Banner'),
        ),
        migrations.AlterField(
            model_name='sportssuspension',
            name='second_section_image',
            field=models.ImageField(blank=True, help_text='Optional - recommended to use an image with a transparent background.', null=True, upload_to='Our_Services/Car_Programming/second_section_image/', verbose_name='Second Section Image'),
        ),
        migrations.AlterField(
            model_name='sportssuspensionslider',
            name='slider_image',
            field=models.ImageField(blank=True, help_text='Optional - you can upload an image or leave it blank. <br> If no image is selected, a default image will be displayed.', null=True, upload_to='Our_Services/Car_Programming/slider_image/', verbose_name='Slider Image'),
        ),
        migrations.AlterField(
            model_name='thermalandsoundinsulation',
            name='first_section_image',
            field=models.ImageField(blank=True, help_text='Optional - recommended to use an image with a transparent background.', null=True, upload_to='Our_Services/Thermal_And_Sound_Insulation/first_section_image/', verbose_name='First Section Image'),
        ),
        migrations.AlterField(
            model_name='thermalandsoundinsulation',
            name='image_banner',
            field=models.ImageField(blank=True, help_text='Optional - you can upload an image or leave it blank. <br> If no image is selected, a default image will be displayed.', null=True, upload_to='Our_Services/Thermal_And_Sound_Insulation/image_banner/', verbose_name='Image Banner'),
        ),
        migrations.AlterField(
            model_name='thermalandsoundinsulation',
            name='second_section_image',
            field=models.ImageField(blank=True, help_text='Optional - recommended to use an image with a transparent background.', null=True, upload_to='Our_Services/Thermal_And_Sound_Insulation/second_section_image/', verbose_name='Second Section Image'),
        ),
        migrations.AlterField(
            model_name='thermalandsoundinsulationslider',
            name='slider_image',
            field=models.ImageField(blank=True, help_text='Optional - you can upload an image or leave it blank. <br> If no image is selected, a default image will be displayed.', null=True, upload_to='Our_Services/Thermal_And_Sound_Insulation/slider_image/', verbose_name='Slider Image'),
        ),
    ]
