

In this task the robot will slide the plate left and right.
This should require 3-4 lines of code.

Please type the name of your function here: `
`
"""

def plate_slide(robot):

    # Steps:
    #  1. Put gripper above the plate
    #  2. Push gripper into left of plate
    #  3. Slide plate to goal

    # The robot can slide the plate by pushing on it.
    # If the plate isn't left of the gripper, move the gripper
    # left of the plate.
    if check("the robot's gripper is not left of the plate"):
        robot.put("gripper left of plate")
    # If the plate is left of the robot's gripper, push the plate.
    if check("the robot's gripper is left of the plate"):
        robot.push("gripper into the plate")
    # If the plate is near the robot's gripper, we have probably trapped it and
    # can slide it to the target location.
    if check("the plate is near the robot's gripper"):
        robot.slide("plate into goal")

[eod] [code]# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='\u5185\u5bb9'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='summary',
            field=models.TextField(verbose_name='\u6982\u8981', help_text=b'\u6982\u8981\u6700\u957f255\u4e2a\u5b57\u7b26'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(verbose_name='\