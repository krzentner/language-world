

Note: The gripper is the green square.
"""

from utils import *
from collections import *

def is_above(entity1, entity2):
    return entity1['y'] <= entity2['y'] + entity2['height'] / 2

def is_vertically_aligned(entity1, entity2):
    return entity1['x'] >= entity2['x'] - entity2['width'] / 2 and entity1['x'] <= entity2['x'] + entity2['width'] / 2

def is_left_of(entity1, entity2):
    return entity1['x'] >= entity2['x'] + entity2['width'] / 2

def is_right_of(entity1, entity2):
    return entity1['x'] <= entity2['x'] - entity2['width'] / 2

def is_near(entity1, entity2):
    return entity1['x'] >= entity2['x'] - entity2['width'] / 2 and entity1['x'] <= entity2['x'] + entity2['width'] / 2 and entity1['y'] >= entity2['y'] - entity2['height'] / 2 and entity1['y'] <= entity2['y'] + entity2['height'] / 2

def is_below(entity1, entity2):
    return entity1['y'] >= entity2['y'] + entity2['height'] / 2

def is_aligned(entity1, entity2):
    return is_vertically_aligned(entity1, entity2) and is_near(entity1, entity2)

def is_forward_aligned(entity1, entity2):
    return is_vertically_aligned(entity1, entity2) and not is_near(entity1, entity2)

def is_around(entity1, entity2):
    return is_aligned(entity1, entity2) and (entity1['x'] >= entity2['x'] or entity1['x'] <= entity2['x'] - entity2['width'])

def is_in_front_of(entity1, entity2):
    return is_aligned(entity1, entity2) and is_below(entity1, entity2)

def drawer_close(robot):
    pass
[eod] [code]from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('core.urls')),
    url(r'^admin/', admin.site.urls),