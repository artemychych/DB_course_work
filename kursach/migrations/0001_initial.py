# Generated by Django 3.2.12 on 2022-02-19 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Armour',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('armor', models.SmallIntegerField()),
                ('char_class_id', models.BigIntegerField()),
                ('craft_id', models.BigIntegerField()),
            ],
            options={
                'db_table': 's284720.armour',
            },
        ),
    ]
