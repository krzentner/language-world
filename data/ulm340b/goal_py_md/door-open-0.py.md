
"""

# TODO
# door-open: pull the door open
def door_open(robot):
    # Steps:
    #  1. Put gripper vertically aligned with the door knob, a bit away from the door
    #  2. Approach and open the gripper around the door knob
    #  3. Pull the door open
    if check("the robot's gripper is not vertically aligned with door knob"):
        robot.move_gripper("vertically aligned with the door knob")
    if check("the robot's gripper is vertically aligned with door knob"):
        robot.move_gripper("around door knob", close_gripper=True)
    if check("the robot's gripper is around door knob"):
        robot.move_gripper("horizontally aligned with door knob")

# # TODO
# # door-open: pull the door open
# def door_open(robot):
#     # Steps:
#     #  1. Put gripper vertically aligned with the door knob, a bit away from the door
#     #  2. Approach and open the gripper around the door knob
#     #  3. Pull the door open
#     if check("the robot's gripper is not vertically aligned with door knob"):
#         robot.move_gripper("vertically aligned with the door knob")
#     if check("the robot's gripper is vertically aligned with door knob"):
#         robot.move_gripper("around door knob", close_gripper=True)
#     if check("the robot's gripper is around door knob"):
#         robot.move_gripper("horizontally aligned with door knob")
[eod] [code]from . import (
    users,
    auth,
    files,
    project,
    group,
    tasks,
    notification,
    role,
)

from . import users, auth, files, group, project, tasks, notification, role
[eod] [code]from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^results$', views.results, name='results'),
    url(r'^about$', views.about, name='about'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
