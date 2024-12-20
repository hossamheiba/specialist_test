# Generated by Django 5.1.3 on 2024-11-30 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_alter_faqsection_options_alter_slidersection_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brands',
            options={'verbose_name': '8 - Brands Section', 'verbose_name_plural': '8 - Brands Section'},
        ),
        migrations.AlterModelOptions(
            name='chooseus',
            options={'verbose_name': '7 - ChooseUs Section', 'verbose_name_plural': '7 - ChooseUs Section'},
        ),
        migrations.AlterField(
            model_name='chooseuscard',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='Home_Page/Choose_Us/', verbose_name='Icon'),
        ),
        migrations.AlterField(
            model_name='faqsection',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Home_Page/FAQSection/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='imagebrand',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Home_Page/Brands/', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='servicecard',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='Home_Page/Slider_Section/'),
        ),
        migrations.AlterField(
            model_name='slidercard',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Home_Page/Slider_Card/', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='workcard',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='Home_Page/work_card/', verbose_name='Icon'),
        ),
    ]
