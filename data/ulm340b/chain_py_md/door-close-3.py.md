

'''

#
# SOLUTION:
#

# door-close: push the door closed to the target location
def door_close(robot):
    # Steps:
    #  1. Put gripper above door handle
    #  2. Push the door closed
    # If the gripper is not near the door handle, move it to the door handle.
    if check("the robot's gripper is not above the door handle"):
        robot.place("gripper above door handle")
    # If the robot's gripper is near the door handle we can probably push the door closed.
    if check("the robot's gripper is near the door handle"):
        robot.push("door close")




[eod] [code]from django.urls import path
from .views import (
    ListArticle,
    ArticleDetail,
    AddArticle,
    EditArticle,
    DeleteArticle,
)

app_name = "articles"
urlpatterns = [
    path("article/", ListArticle.as_view(), name="list_articles"),
    path("article/add", AddArticle.as_view(), name="add_articles"),
    path("article/<slug>/", ArticleDetail.as_view(), name="article_detail"),
    path("article/<slug>/edit", EditArticle.as_view(), name="article_edit"),
    path("article/<slug>/delete", DeleteArticle.as_view(), name="article_delete"),
]
[eod] [code]# -*- coding: utf-8 -*-
"""
    tests
    ~~~~~

    :copyright: 2015 by Daniel Neuhäuser
"""

import unittest

import flask

from flask_static_compress import FlaskCompress


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = flask.Flask('')
        self.compress = FlaskCompress(self.app)

    def tearDown(self):
        self.app.pop_http_exception_handlers()

    def test_should_not_set_caching_header_if_compression_disabled(self):
        @self.app.route('/file.css')
        @self.compress.html
        def index():
            return ''

        response = self.app.test_client().get('/')
        self.assertFalse(response.cache_control.no_cache)

    def test_should_set_default_header_if_compression