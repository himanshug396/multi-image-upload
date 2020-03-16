# Generated by Django 3.0.4 on 2020-03-16 17:47

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Claim',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('description', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('claim_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='captureEdge.Claim')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('photo', models.ImageField(upload_to=None)),
                ('claim_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='captureEdge.Claim')),
                ('phone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='captureEdge.Phone')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
