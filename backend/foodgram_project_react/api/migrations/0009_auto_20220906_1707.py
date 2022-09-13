# Generated by Django 2.2.19 on 2022-09-06 17:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0008_auto_20220906_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='ingridients',
            field=models.ManyToManyField(related_name='recipes', to='api.Ingredients', verbose_name='Ингридиенты'),
        ),
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='selectd', to='api.Recipes')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='selecte', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]