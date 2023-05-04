
"""

# drawer-open: pull the drawer open
def drawer_open(robot):
    if check("the robot's gripper is not near the drawer handle"):
        robot.move("gripper to right of handle")
    if check("the robot's gripper is near the drawer handle and not in front of the handle"):
        robot.grab("drawer handle")
    if check("the robot's gripper is in front of the drawer handle"):
        robot.pull("drawer open")
    [eod] [code]import pytest
import random

from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.core import mail
from django.core.management import call_command
from django.test import TestCase, Client
from django.urls import reverse

from django_rq import job
from rest_framework.authtoken.models import Token

from profiles.models import Profile
from .models import Comment, Post, Group, Follow
from .tasks import send_message
from .services import get_profile_image, get_or_create_profile


@job
def send_test_message(request):
    send_message('test', '12345')


@pytest.mark.django_db
class AdminTest(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.test_user = get_user_model().objects.create_user(
            username='test_user',
            password='12345',
            email='test_user@test.com',
        )
        self.admin_user = get_user_model().objects.create_superuser(
            username='admin_user',
            password='12345',
            email='admin_user@test.com',
        )
        get_or_create_profile(self.test_user)
        get_or_create_profile(self.admin_user)

    def test_auth_user(self):
        self.client.force_login(self.admin_user)
        response = self.client.post(
            reverse('admin:core_authuser_changelist'),
            data={
                'username': 'test_user',
                'password': '12345'
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual