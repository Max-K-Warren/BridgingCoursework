# Generated by Django 2.2.13 on 2020-08-28 00:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CV_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('position', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CV_Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('position', models.IntegerField()),
                ('CV_Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cv.CV_Category')),
            ],
        ),
    ]
