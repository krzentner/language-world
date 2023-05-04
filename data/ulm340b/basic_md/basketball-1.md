
    - When the robot's gripper is not near the ball, the robot should grasp ball.
    - When the ball is above the robot's gripper, the robot should lift the ball above the hoop.
    - When the ball is at the hoop height, the robot should release gripper.

The task `window-close-v2` requires the robot to slide the window closed to the right.
To slide the window closed to the right reliably, the robot should perform the following steps:
    - When the window handle is right of the robot's gripper and the robot's gripper is not near the window handle, the robot should move gripper to left of window handle.
    - When the robot's gripper is near the window handle, the robot should slide window right.
    - When the robot's gripper is in front of the window handle, the robot should push window right harder.

The task `door-open-v2` requires the robot to pull the door open.
To pull the door open reliably, the robot should perform the following steps:
    - When the robot's gripper is not near the door handle, the robot should move to the door handle.
    - When the robot's gripper is near the door handle, the robot should put gripper around door handle.
    - When the robot's gripper is around door handle, the robot should pull the door open.
"""

TASKS_FOR_TEST = """
    reach
    door-open
    drawer-close
    push
    button-press-topdown
    drawer-open
    pick-place
    window-close
    window-open
    peg-insert-side
    basketball
    window-close-v2
    door-open-v2
""".strip().split()
[eod] [code]"""
WSGI config for blog_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_project.settings')

application = get_wsgi_application()
[eod] [code]#!/usr/bin/env python3
"""
 Copyright 2020 Hung-Hsin Chen, LSA Lab, National Tsing Hua University

 Licensed under the Apache License, Version 2.0 (the "License");
 you may