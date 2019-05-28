# -*- coding: utf-8 -*-


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='GridColumnFoundation',
            fields=[
                ('size_small', models.IntegerField(default=0, null=True, verbose_name='size (mobile)', blank=True, choices=[(1, '1 columns'), (2, '2 columns'), (3, '3 columns'), (4, '4 columns'), (5, '5 columns'), (6, '6 columns'), (7, '7 columns'), (8, '8 columns'), (9, '9 columns'), (10, '10 columns'), (11, '11 columns'), (12, '12 columns'), (13, '13 columns'), (14, '14 columns'), (15, '15 columns'), (16, '16 columns'), (17, '17 columns'), (18, '18 columns'), (19, '19 columns'), (20, '20 columns'), (21, '21 columns'), (22, '22 columns'), (23, '23 columns'), (24, '24 columns')])),
                ('size_medium', models.IntegerField(default=0, null=True, verbose_name='size (tablet)', blank=True, choices=[(1, '1 columns'), (2, '2 columns'), (3, '3 columns'), (4, '4 columns'), (5, '5 columns'), (6, '6 columns'), (7, '7 columns'), (8, '8 columns'), (9, '9 columns'), (10, '10 columns'), (11, '11 columns'), (12, '12 columns'), (13, '13 columns'), (14, '14 columns'), (15, '15 columns'), (16, '16 columns'), (17, '17 columns'), (18, '18 columns'), (19, '19 columns'), (20, '20 columns'), (21, '21 columns'), (22, '22 columns'), (23, '23 columns'), (24, '24 columns')])),
                ('size_large', models.IntegerField(default=0, null=True, verbose_name='size (desktop)', blank=True, choices=[(1, '1 columns'), (2, '2 columns'), (3, '3 columns'), (4, '4 columns'), (5, '5 columns'), (6, '6 columns'), (7, '7 columns'), (8, '8 columns'), (9, '9 columns'), (10, '10 columns'), (11, '11 columns'), (12, '12 columns'), (13, '13 columns'), (14, '14 columns'), (15, '15 columns'), (16, '16 columns'), (17, '17 columns'), (18, '18 columns'), (19, '19 columns'), (20, '20 columns'), (21, '21 columns'), (22, '22 columns'), (23, '23 columns'), (24, '24 columns')])),
                ('custom_classes', models.CharField(max_length=200, verbose_name='custom classes', blank=True)),
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='aldryn_grid_foundation_gridcolumnfoundation', primary_key=True, serialize=False, to='cms.CMSPlugin', on_delete=models.deletion.CASCASE)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='GridFoundation',
            fields=[
                ('custom_classes', models.CharField(max_length=200, verbose_name='custom classes', blank=True)),
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='aldryn_grid_foundation_gridfoundation', primary_key=True, serialize=False, to='cms.CMSPlugin', on_delete=models.deletion.CASCASE)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
