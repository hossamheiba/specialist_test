# Generated by Django 5.1.3 on 2024-11-28 08:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FaqSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_banner', models.ImageField(blank=True, help_text='Optional - you can upload an image or leave it blank. <br> If no image is selected, a default image will be displayed.', null=True, upload_to='Our_Services/Electricity/image_banner/', verbose_name='Image Banner')),
                ('title', models.CharField(blank=True, help_text='Maximum 50 characters', max_length=50, null=True, verbose_name='Section Title')),
                ('title_ar', models.CharField(blank=True, help_text='Maximum 50 characters', max_length=50, null=True, verbose_name='Section Title')),
                ('title_en', models.CharField(blank=True, help_text='Maximum 50 characters', max_length=50, null=True, verbose_name='Section Title')),
                ('description', models.TextField(blank=True, help_text='Description of the first section', null=True, verbose_name='Description')),
                ('description_ar', models.TextField(blank=True, help_text='Description of the first section', null=True, verbose_name='Description')),
                ('description_en', models.TextField(blank=True, help_text='Description of the first section', null=True, verbose_name='Description')),
                ('image', models.ImageField(blank=True, help_text='Optional - recommended to use an image with a transparent background.', null=True, upload_to='Our_Services/Electricity/first_section_image/', verbose_name='First Section Image')),
            ],
            options={
                'verbose_name': 'Faq Section',
                'verbose_name_plural': 'Faq Sections',
            },
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(blank=True, null=True, verbose_name='Question')),
                ('question_ar', models.TextField(blank=True, null=True, verbose_name='Question')),
                ('question_en', models.TextField(blank=True, null=True, verbose_name='Question')),
                ('answer', models.TextField(blank=True, null=True, verbose_name='Answer')),
                ('answer_ar', models.TextField(blank=True, null=True, verbose_name='Answer')),
                ('answer_en', models.TextField(blank=True, null=True, verbose_name='Answer')),
                ('faq_section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='faqs', to='FAQ.faqsection')),
            ],
            options={
                'verbose_name': 'FAQ',
                'verbose_name_plural': 'FAQs',
            },
        ),
    ]