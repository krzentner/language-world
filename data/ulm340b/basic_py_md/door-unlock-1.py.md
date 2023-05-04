
"""

# TASK: FILL IN THE BLANK IN THIS PROCEDURE
# def door_unlock(robot):
#     if check("the robot's gripper is not vertically aligned with dial"):
#         robot.put("gripper above dial")
#     if check("the robot's gripper is not vertically aligned with dial and the robot's gripper is open"):
#         robot.put("gripper around dial")
#     if check("the robot's gripper is around dial"):
#         robot.turn("dial clockwise")
#         robot.turn("dial counter-clockwise")
#         robot.turn("dial counter-clockwise")
#         robot.turn("dial clockwise")
#         robot.turn("dial clockwise")
#         robot.turn("dial clockwise")
#         robot.turn("dial clockwise")
#         robot.turn("dial clockwise")
#         robot.turn("dial clockwise")


def door_unlock(robot):
    if check("the robot's gripper is not vertically aligned with dial"):
        robot.put("gripper above dial")
    if check("the robot's gripper is vertically aligned with dial and the robot's gripper is open"):
        robot.put("gripper around dial")
    if check("the robot's gripper is around dial"):
        robot.turn("dial clockwise")
        robot.turn("dial counter-clockwise")
        robot.turn("dial counter-clockwise")
        robot.turn("dial clockwise")
        robot.turn("dial clockwise")
        robot.turn("dial clockwise")
        robot.turn("dial clockwise")
        robot.turn("dial clockwise")
        robot.turn("dial clockwise")


# TASK: TEST YOUR PROCEDURE HERE
# door_unlock(robot)


def main():
    print("Instructions:")
    for func in robot.func_map:
        print("   " + func)


main()

[eod] [code]# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0037_auto_20150414_0018'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSettings',
            fields=[
                ('id', models