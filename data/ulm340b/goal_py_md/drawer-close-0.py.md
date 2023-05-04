

# Write your program here (we are not collecting it):

import numpy as np
np.set_printoptions(suppress=True)

# drawer-close: push the drawer close
def drawer_close(robot):
    # Steps:
    #  1. Put gripper vertically aligned with drawer handle
    #  2. Drop gripper around drawer handle
    #  3. Push closed the drawer

    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.move_gripper("vertically aligned with the drawer handle")

    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around drawer handle"):
        robot.move_gripper("around the drawer handle", close_gripper=True)

    if check("the robot's gripper is around drawer handle"):
        robot.move_gripper("horizontally aligned with the drawer handle")
'''

# Test if your program works:

print(drawer_close(Robot("drawer-close")))

print('\n\nThanks! Have a good day.')[eod] [code]# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name_plural': 'clients'},
        ),
        migrations.AlterModelOptions(
            name='device',
            options={'verbose_name_plural': 'devices'},
        ),
        migrations.AlterField(
            model_name='client',
            name='device_types',
            field=models.ManyToManyField(to='portal.DeviceType'),
        ),
        migrations.AlterField(
            model_name='client',
            name='operating_systems',
            field=models.ManyToManyField(to='portal.OperatingSystem'),
        ),
        migrations.AlterField(
            model_name='device',
            name='clients',
            field=models.ForeignKey(to='portal.Client'),
        ),
        migrations.AlterField(
            model_name='device',
            name='operating_system',
            field=models.ForeignKey(to='portal.OperatingSystem'),
        ),
    ]
[eod]