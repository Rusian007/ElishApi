# Generated by Django 4.0.2 on 2023-02-07 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Routes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
        migrations.AlterField(
            model_name='route',
            name='endingpoint',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ending_point', to='Routes.point'),
        ),
        migrations.AlterField(
            model_name='route',
            name='starting_point',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='starting_point', to='Routes.point'),
        ),
    ]