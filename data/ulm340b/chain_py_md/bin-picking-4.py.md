

and complete the rest of the program.

'''

# 49.7% of workers

# Steps:
#  1. Put gripper above cube
#  2. Drop gripper around cube
#  3. Close gripper around cube
#  4. Put the cube into the target bin

# First, put the gripper roughly above cube, so that we don't bump it while
# trying to grab it.
if check("the robot's gripper is not above the cube"):
    robot.place("gripper above cube")
# If the gripper isn't around the cube, put it around the cube.
if check("the robot's gripper is not around cube and the robot's gripper is open"):
    robot.drop("gripper around cube")
# If the gripper is near the cube and open, maybe we can grab it by closing
# the gripper.
if check("the robot's gripper is near cube and the robot's gripper is open"):
    robot.close("gripper around cube")
# We closed the gripper, and the cube is still near the gripper, so maybe we
# grabbed it.
# Try to put the cube into the goal.
# If we didn't grab it, we'll just go back to an earlier step.
if check("the robot's gripper is above cube and the robot's gripper is closed"):
    robot.place("cube at goal")
[eod] [code]# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-08 21:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('intro', wagtail.core.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,