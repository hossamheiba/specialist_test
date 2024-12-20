# Generated by Django 5.1.3 on 2024-11-26 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('About_Us', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutsection',
            name='shape_image_1',
        ),
        migrations.RemoveField(
            model_name='aboutsection',
            name='shape_image_2',
        ),
        migrations.AddField(
            model_name='aboutsection',
            name='image_banner',
            field=models.ImageField(blank=True, help_text='Optional - you can upload an image or leave it blank. <br> If no image is selected, a default image will be displayed.', null=True, upload_to='Our_Services/Mechanics/image_banner/', verbose_name='Image Banner'),
        ),
    ]
