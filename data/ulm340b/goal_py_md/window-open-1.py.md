

## 7
"""

# window-open: slide the window open to the left
def window_open(robot):
    # Steps:
    #  1. Put gripper near the window handle
    #  2. Start pushing against the window handle to open the window
    #  3. Push the window open harder
    # If the the window handle is left of the robot's gripper, we should move the
    # gripper near the window handle to start pushing
    if check("the robot's gripper is in front of the window handle"):
        robot.move_gripper("left of the window handle")
    # If the robot's gripper is near the window handle we can probably slide the
    # window open now by moving the gripper left.
    if check("the window handle is left of the robot's gripper and the robot's gripper is not near the window handle"):
        robot.move_gripper("almost vertically aligned with the window handle")
    # If the robot's gripper is starting to be in front of the window handle,
    # push harder.
    if check("the robot's gripper is near the window handle"):
        robot.move_gripper("forward aligned with the window handle")
[eod] [code]from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import redirect_to_login
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views import generic

from . import forms, models, utils


def login_not_required(view_func):
    """
    Decorator for views that marks view as not requiring login.

    Taken from `django.contrib.auth.decorators`

    It only sets the login_url attribute of the class based view
    """
    view_func.login_url = None
    return view_func


class ListView(LoginRequiredMixin, generic.ListView):
    model = models.Job
    context_object_name = 'jobs'
    paginate_by = 20


class DetailView(LoginRequiredMixin, generic.DetailView):
    model = models.Job
    slug_field = 'slug'
    slug_url_kwarg = 