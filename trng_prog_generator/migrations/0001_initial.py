# Generated by Django 2.1.7 on 2019-03-12 08:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_still_trng', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('athlete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Athlete', to='trng_prog_generator.Athlete')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Programme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('training_mode', models.TextField(max_length=150)),
                ('created_by_coach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coach_create', to='trng_prog_generator.Coach')),
                ('updated_by_coach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coach_update', to='trng_prog_generator.Coach')),
                ('view_by_athlete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='athlete_view', to='trng_prog_generator.Athlete')),
            ],
        ),
    ]
