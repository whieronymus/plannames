# Generated by Django 2.0 on 2017-12-14 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('number', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='plan',
            unique_together={('name', 'number')},
        ),
    ]
