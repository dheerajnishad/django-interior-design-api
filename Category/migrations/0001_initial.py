# Generated by Django 2.2.6 on 2020-03-20 13:29

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('Id', models.IntegerField(default=1)),
                ('CategoryId', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('Name', models.CharField(blank=True, default=None, max_length=1000, null=True)),
                ('DisplayOrder', models.IntegerField()),
                ('isActive', models.BooleanField(default=False)),
                ('ParentCategoryID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='SubCategory', to='Category.Category')),
            ],
        ),
    ]