
    # Steps:
    #  1. Put gripper above peg
    #  2. Grab the peg
    #  3. Pull the wrench up
    #  4. Move the wrench away from the peg
    # First, put the gripper roughly above the peg, so that we don't bump the
    # peg while trying to grab it.
    if check("the robot's gripper is not above the peg"):
        robot.move_gripper("above the peg")
    # If the gripper is not around the peg, put it around the peg.
    if check("the robot's gripper is not around peg and the robot's gripper is open"):
        robot.move_gripper("around the peg", close_gripper=True)
    # If the gripper is around the peg and closed, start pulling the wrench up.
    if check("the robot's gripper is above the peg"):
        robot.move_gripper("forward aligned with the peg")
    # If the wrench is almost pulled out from the peg, move the gripper away
    # from the peg.
    if check("the wrench is above the peg and the peg is left of the robot's gripper"):
        robot.move_gripper("right of the peg", open_gripper=True)
[eod] [code]"""
WSGI config for django_tutorial_prj project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_tutorial_prj.settings')

application = get_wsgi_application()
[eod] [code]from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def hello(request):
    return render(request, 'hello.html')
[eod] [code]from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib