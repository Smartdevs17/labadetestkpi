# Generated by Django 3.2.12 on 2022-03-18 23:14

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mkpd',
            name='remark',
        ),
        migrations.AddField(
            model_name='mkpd',
            name='skpd',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='hrms.skpd'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='bank_id',
            field=models.CharField(default='bank159', max_length=70, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='designation',
            name='design_id',
            field=models.CharField(default='design627', max_length=70, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_id',
            field=models.CharField(default='emp394', max_length=70),
        ),
        migrations.AlterField(
            model_name='employeetype',
            name='employeetype_id',
            field=models.CharField(default='emptype720', max_length=70, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employment',
            name='employ_id',
            field=models.CharField(default='emp5549', max_length=70, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='kpd',
            name='period',
            field=models.DateField(choices=[(datetime.date(2022, 3, 1), 'P:3:2022'), (datetime.date(2022, 4, 1), 'P:4:2022'), (datetime.date(2022, 5, 1), 'P:5:2022'), (datetime.date(2022, 6, 1), 'P:6:2022'), (datetime.date(2022, 7, 1), 'P:7:2022'), (datetime.date(2022, 8, 1), 'P:8:2022'), (datetime.date(2022, 9, 1), 'P:9:2022'), (datetime.date(2022, 10, 1), 'P:10:2022'), (datetime.date(2022, 11, 1), 'P:11:2022'), (datetime.date(2022, 12, 1), 'P:12:2022')], max_length=70),
        ),
        migrations.AlterField(
            model_name='position',
            name='position_code',
            field=models.CharField(default='pc145', max_length=70, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='sbu_directorate',
            name='sbu_id',
            field=models.CharField(default='sub569', max_length=70, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='skpd',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff', to='hrms.employment'),
        ),
        migrations.AlterField(
            model_name='skpd',
            name='kpd',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff_kpd', to='hrms.kpd'),
        ),
        migrations.AlterField(
            model_name='skpd',
            name='period',
            field=models.DateField(choices=[(datetime.date(2022, 3, 1), 'P:3:2022'), (datetime.date(2022, 4, 1), 'P:4:2022'), (datetime.date(2022, 5, 1), 'P:5:2022'), (datetime.date(2022, 6, 1), 'P:6:2022'), (datetime.date(2022, 7, 1), 'P:7:2022'), (datetime.date(2022, 8, 1), 'P:8:2022'), (datetime.date(2022, 9, 1), 'P:9:2022'), (datetime.date(2022, 10, 1), 'P:10:2022'), (datetime.date(2022, 11, 1), 'P:11:2022'), (datetime.date(2022, 12, 1), 'P:12:2022')], max_length=70),
        ),
        migrations.AlterField(
            model_name='unit',
            name='unit_id',
            field=models.CharField(default='unit626', max_length=70, primary_key=True, serialize=False),
        ),
    ]
