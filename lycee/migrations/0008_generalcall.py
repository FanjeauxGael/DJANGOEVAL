# Generated by Django 3.1.7 on 2021-04-10 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lycee', '0007_auto_20210410_1132'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralCall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateTimeField()),
                ('cursus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lycee.cursus')),
            ],
        ),
    ]
