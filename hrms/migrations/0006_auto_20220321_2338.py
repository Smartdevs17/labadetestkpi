# Generated by Django 3.2.12 on 2022-03-21 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0005_auto_20220321_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='bank_id',
            field=models.CharField(default='bank843', max_length=70, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='designation',
            name='design_id',
            field=models.CharField(default='design433', max_length=70, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_id',
            field=models.CharField(default='emp639', max_length=70),
        ),
        migrations.AlterField(
            model_name='employeetype',
            name='employeetype_id',
            field=models.CharField(default='emptype652', max_length=70, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employment',
            name='employ_id',
            field=models.CharField(default='emp1083', max_length=70, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='kpi_evalutation',
            name='comment',
            field=models.CharField(choices=[('excellent', 'EXCELLENT'), ('very good', 'VERY GOOD'), ('good', 'GOOD'), ('satisfactory', 'SATISFACTORY'), ('unsatisfactory', 'UNSATISFACTORY')], max_length=200),
        ),
        migrations.AlterField(
            model_name='position',
            name='position_code',
            field=models.CharField(default='pc752', max_length=70, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='sbu_directorate',
            name='sbu_id',
            field=models.CharField(default='sub365', max_length=70, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='unit',
            name='unit_id',
            field=models.CharField(default='unit956', max_length=70, primary_key=True, serialize=False),
        ),
    ]
