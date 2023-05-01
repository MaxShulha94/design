# Generated by Django 4.2 on 2023-04-13 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projectcategory',
            options={'ordering': ('position',)},
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=20)),
                ('category_name', models.CharField(max_length=20)),
                ('text', models.CharField(max_length=100)),
                ('project_name', models.CharField(max_length=20, unique=True)),
                ('photo', models.ImageField(upload_to='projects_photo')),
                ('description', models.TextField(blank=True, max_length=300)),
                ('position', models.PositiveSmallIntegerField(unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.projectcategory')),
            ],
            options={
                'ordering': ('position',),
            },
        ),
    ]