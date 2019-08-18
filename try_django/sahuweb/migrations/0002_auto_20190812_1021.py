# Generated by Django 2.2.3 on 2019-08-12 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sahuweb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
                ('city', models.IntegerField()),
                ('favourite', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='destination',
        ),
    ]