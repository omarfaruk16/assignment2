# Generated by Django 4.2.9 on 2024-06-23 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_alter_todomodel_description_alter_todomodel_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formname', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='todomodel',
            name='description',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='todomodel',
            name='status',
            field=models.CharField(choices=[('incomplete', 'Incomplete')], default='incomplete', max_length=10),
        ),
        migrations.AlterField(
            model_name='todomodel',
            name='title',
            field=models.CharField(max_length=20),
        ),
    ]
