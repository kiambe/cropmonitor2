# Generated by Django 4.1.1 on 2022-09-21 11:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('farm', '0002_alter_myfarm_vc_variety'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telephone', models.IntegerField(blank=True, null=True)),
                ('mobile', models.IntegerField(blank=True, null=True)),
                ('year_of_birth', models.PositiveIntegerField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=6, null=True)),
                ('county', models.CharField(blank=True, max_length=20, null=True)),
                ('subcounty', models.CharField(blank=True, max_length=20, null=True)),
                ('ward', models.CharField(blank=True, max_length=20, null=True)),
                ('lat', models.FloatField(blank=True, max_length=20, null=True)),
                ('lon', models.FloatField(blank=True, max_length=20, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
