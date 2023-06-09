# Generated by Django 4.2.1 on 2023-05-07 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('access', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('there', models.CharField(max_length=221)),
                ('more_info', models.TextField()),
                ('number', models.CharField(blank=True, max_length=221, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SocialLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=221, null=True)),
                ('url', models.CharField(max_length=221)),
            ],
        ),
        migrations.CreateModel(
            name='UserSocialLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SocialLink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.sociallink')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='access.user')),
            ],
        ),
    ]
