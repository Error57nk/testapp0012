# Generated by Django 3.1 on 2021-07-19 17:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoStoreModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='pstore/photo/')),
                ('desc', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='OrderFormModel',
            fields=[
                ('orderId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('changeType', models.TextField(max_length=100)),
                ('note', models.TextField(blank=True, max_length=200)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('orderfrom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('picture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pstore.photostoremodel')),
            ],
        ),
    ]
