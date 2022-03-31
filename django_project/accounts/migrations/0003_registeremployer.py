# Generated by Django 4.0 on 2022-01-02 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_rename_jobtype_registercandidate_jobtypes'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterEmployer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('company_email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('state', models.TextField()),
                ('pincode', models.IntegerField()),
                ('contactno', models.IntegerField()),
                ('work_hours', models.TextField()),
                ('jobtypes', models.TextField()),
                ('skills', models.TextField()),
                ('salary', models.TextField()),
                ('comments', models.TextField()),
            ],
        ),
    ]