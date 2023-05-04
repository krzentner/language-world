

Then, you will need to add a series of instructions to the robot, using the words from our language in the right order.
Use the word "put" first.
Then, use the word "pull", and then the word "away".
Then, use a word to describe the thing you want to pull it away from.

'''


# 5.17
'''
# robot-pick-place: pick up the robot and hold it at the target location
def robot_pick_place(robot):
    if check("the robot's gripper is not above the robot"):
        robot.put("gripper above robot")
    if check("the robot's gripper is not around robot and the robot's gripper is open"):
        robot.drop("gripper around robot")
    if check("the robot's gripper is near robot and the robot's gripper is open"):
        robot.close("gripper around robot")
    if check("the robot's gripper is above robot and the robot's gripper is closed"):
        robot.place("robot at goal")

# door-open: pull the door open
def door_open(robot):
    if check("the robot's gripper is not vertically aligned with door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is vertically aligned with door handle and the robot's gripper is not around door handle"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is around door handle"):
        robot.pull("away from door")
'''
[eod] [code]from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/', views.admin_view, name='admin_view'),
    path('', include('core.urls')),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )[eod] [code]"""
WSGI config for api_scrapping project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

