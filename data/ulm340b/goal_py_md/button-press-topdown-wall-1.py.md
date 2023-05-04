

## Step 4

You now have completed your work. You will be given a chance to review your answers and then submit them.

```
    # Steps:
    #  1. Put the gripper above button
    #  2. Start pushing against the wall
    #  3. Keep pushing against the wall until you're near the button
    if check("the robot's gripper is not vertically aligned with the button"):
        robot.move_gripper("almost vertically aligned with button")
    if check("the robot's gripper is vertically aligned with the button and the robot's gripper is not near the button"):
        robot.move_gripper("above the button")

```
[eod] [code]import pandas as pd


class InputData:
    
    def __init__(self):
        pass

    @staticmethod
    def load_csv(filename, index_col):
        df = pd.read_csv(filename, index_col=index_col)
        df.dropna(axis=1, how='all', inplace=True)
        df.dropna(axis=0, how='all', inplace=True)
        return df
[eod] [code]from django.db import models

class Article(models.Model):
    subject = models.CharField(max_length = 50)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.subject[eod] [code]"""
WSGI config for backend_app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_app.settings')

application = get_wsgi_application()
[eod] [code]def get_int():
    integer = int(input())
    return integer

def main():
    n = get_int()
    print(n)

main()
[eod] [code]"""

"""
import logging
from typing import Any, Dict, Union

import 