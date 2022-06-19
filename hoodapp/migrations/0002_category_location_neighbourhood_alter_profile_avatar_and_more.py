# Generated by Django 4.0.5 on 2022-06-19 09:23

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hoodapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Neighbourhood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hoodapp.location')),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=280)),
                ('category', models.CharField(default='General', max_length=50)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hoodapp.profile')),
                ('hood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hoodapp.neighbourhood')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=50)),
                ('comment_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hoodapp.profile')),
                ('comment_on', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hoodapp.post')),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('tel', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hoodapp.category')),
                ('hood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hoodapp.neighbourhood')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hoodapp.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Amenities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('tel', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('amenity_type', models.CharField(max_length=50)),
                ('hood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hoodapp.neighbourhood')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='neighbourhood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hoodapp.neighbourhood'),
        ),
    ]