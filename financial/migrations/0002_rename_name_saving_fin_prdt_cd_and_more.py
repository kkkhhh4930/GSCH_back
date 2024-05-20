# Generated by Django 4.2.7 on 2024-05-20 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='saving',
            old_name='name',
            new_name='fin_prdt_cd',
        ),
        migrations.RenameField(
            model_name='saving',
            old_name='saving_code',
            new_name='fin_prdt_nm',
        ),
        migrations.RemoveField(
            model_name='deposit',
            name='contract_user',
        ),
        migrations.RemoveField(
            model_name='deposit',
            name='dcls_month',
        ),
        migrations.RemoveField(
            model_name='deposit',
            name='fin_co_no',
        ),
        migrations.RemoveField(
            model_name='deposit',
            name='max_limit',
        ),
        migrations.RemoveField(
            model_name='deposit',
            name='mtrt_int',
        ),
        migrations.AlterField(
            model_name='deposit',
            name='etc_note',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='fin_prdt_cd',
            field=models.TextField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='fin_prdt_nm',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='join_deny',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='join_member',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='join_way',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='kor_co_nm',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='spcl_cnd',
            field=models.TextField(null=True),
        ),
    ]
