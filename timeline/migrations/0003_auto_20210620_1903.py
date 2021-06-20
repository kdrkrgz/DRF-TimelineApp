# Generated by Django 3.2.4 on 2021-06-20 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0002_alter_userprofile_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timelinemessage',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='timelinemessage',
            name='deleted_date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='timelinemessage',
            name='updated_date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='deleted_date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usersinteam', to='timeline.userteam'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='updated_date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='userteam',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='userteam',
            name='deleted_date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='userteam',
            name='updated_date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]