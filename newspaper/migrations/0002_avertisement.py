# Generated by Django 5.2.1 on 2025-06-25 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='advertisements/%Y/%m/%d')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
