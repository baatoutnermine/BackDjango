# Generated by Django 4.2.3 on 2023-07-14 01:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categorie', '0001_initial'),
        ('image', '0003_alter_image_description_alter_image_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='categorie',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='categorie.categorie'),
        ),
    ]