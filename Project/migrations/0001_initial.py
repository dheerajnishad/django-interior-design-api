# Generated by Django 2.2.6 on 2020-03-20 13:29

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('Id', models.IntegerField(default=1)),
                ('ProjectId', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('Name', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('Description', models.CharField(blank=True, default=None, max_length=10000, null=True)),
                ('DisplayOrder', models.IntegerField()),
                ('isActive', models.BooleanField(default=False)),
                ('CategoryId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Category', to='Category.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('FileName', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('ProjectId', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Images', to='Project.Project')),
            ],
        ),
    ]
