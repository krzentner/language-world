

and fill in the rest of the program below.

'''

__author__ = 'Jonathan S. Rosenfeld'
__copyright__ = 'Copyright 2018, Jonathan S. Rosenfeld'
__license__ = 'MIT'
__credits__ = ['Benjamin Krieger', 'Jonathan S. Rosenfeld']
__version__ = '2.0.0'

# Robot program for coffee-button
#
# Steps:
#  1. Put gripper above button
#  2. Drop gripper around button
#  3. Close gripper around button
#  4. Press button
if check("the robot's gripper is not almost vertically aligned with button"):
    robot.move_gripper("almost vertically aligned with the button", close_gripper=True)
if check("the robot's gripper is vertically aligned with button"):
    robot.move_gripper("near the button")
if check("the robot's gripper is vertically aligned with button"):
    robot.move_gripper("above the button")
if check("the robot's gripper is vertically aligned with button"):
    robot.move_gripper("almost vertically aligned with the button")

[eod] [code]# coding: utf-8
import json
import logging
from uuid import uuid4
from datetime import datetime

import jwt
import requests
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import logout as django_logout
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model
from django.db import transaction
from django.shortcuts import redirect, reverse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
)
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

from common.mixins import SuperuserOrAdminRequiredMixin
from common.pagination import StandardResultPagination
from common.permissions import IsAccountOwner
from common.utils import generate_password_reset_token
from common.utils import is_password_reset_token_expired
from common.utils.api import create_or_update_object
from common.utils.api import get_objects_list
from common.utils.