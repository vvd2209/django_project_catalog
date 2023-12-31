# Generated by Django 4.2.7 on 2023-11-23 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='контакты')),
            ],
            options={
                'verbose_name': 'контакт',
                'verbose_name_plural': 'контакты',
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='category',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='изображение'),
        ),
    ]
