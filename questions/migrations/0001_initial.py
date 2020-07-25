# Generated by Django 3.0.7 on 2020-07-16 04:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='questions',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=1200)),
            ],
        ),
    ]