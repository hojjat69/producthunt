# Generated by Django 2.2.7 on 2019-12-16 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('votes_total', models.IntegerField()),
                ('icon', models.ImageField(upload_to='medial/')),
                ('hunter', models.CharField(max_length=200)),
                ('body', models.TextField(max_length=1500)),
            ],
        ),
    ]