# Generated by Django 4.2.3 on 2023-07-13 23:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categorie', '0001_initial'),
        ('image', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='categorie',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='categorie.categorie'),
        ),
        migrations.AddField(
            model_name='image',
            name='tags',
            field=models.CharField(choices=[('fleurs', 'FLEURS'), ('voiture', 'VOITURE'), ('plage', 'PLAGE')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
