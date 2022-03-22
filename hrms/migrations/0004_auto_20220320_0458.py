# Generated by Django 3.2.12 on 2022-03-20 04:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0003_auto_20220320_0453'),
    ]

    operations = [
        migrations.AddField(
            model_name='kpi_evalutation',
            name='period',
            field=models.DateField(choices=[(datetime.date(2022, 3, 1), 'P:3:2022'), (datetime.date(2022, 4, 1), 'P:4:2022'), (datetime.date(2022, 5, 1), 'P:5:2022'), (datetime.date(2022, 6, 1), 'P:6:2022'), (datetime.date(2022, 7, 1), 'P:7:2022'), (datetime.date(2022, 8, 1), 'P:8:2022'), (datetime.date(2022, 9, 1), 'P:9:2022'), (datetime.date(2022, 10, 1), 'P:10:2022'), (datetime.date(2022, 11, 1), 'P:11:2022'), (datetime.date(2022, 12, 1), 'P:12:2022')], default=datetime.date.today, max_length=70),
        ),
        migrations.AlterField(
            model_name='bank',
            name='bank_id',
            field=models.CharField(default='bank901', max_length=70, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='designation',
            name='design_id',
            field=models.CharField(default='design941', max_length=70, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_id',
            field=models.CharField(default='emp901', max_length=70),
        ),
        migrations.AlterField(
            model_name='employeetype',
            name='employeetype_id',
            field=models.CharField(default='emptype245', max_length=70, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employment',
            name='employ_id',
            field=models.CharField(default='emp8234', max_length=70, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='position',
            name='position_code',
            field=models.CharField(default='pc584', max_length=70, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='sbu_directorate',
            name='sbu_id',
            field=models.CharField(default='sub602', max_length=70, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='unit',
            name='unit_id',
            field=models.CharField(default='unit433', max_length=70, primary_key=True, serialize=False),
        ),
    ]