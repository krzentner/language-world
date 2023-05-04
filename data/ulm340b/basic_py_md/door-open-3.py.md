
"""

# door-open: pull the door open
def door_open(robot):
    if check("the robot's gripper is not vertically aligned with door handle"):
        robot.put("gripper above door handle")
    if check("the robot's gripper is vertically aligned with door handle and the robot's gripper is not around door handle"):
        robot.put("gripper around door handle")
    if check("the robot's gripper is around door handle"):
        robot.pull("away from door")
[eod] [code]from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')[eod] [code]from selenium.webdriver.support.ui import Select


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def switch_to_frame(self, name_or_id):
        self.driver.switch_to.frame(name_or_id)

    def select_option_by_visible_text(self, id_or_name, value):
        select_drop_list = Select(self.driver.find_element_by_id(id_or_name))
        select_drop_list.select_by_visible_text(value)

    def select_option_by_value(self, id_or_name, value):
        select_drop_list = Select(self.driver.find_element_by_id(id_or_name))
        select_drop_list.select_by_value(value)

    def click(self, locator):
        element = self.driver.find_element(*locator)
        element.click()

    def send_keys(self, locator, text):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)
[eod] [code]import pytest
import pandas as pd
import geopandas as gpd
import geobr


def test_read_region():

    assert geobr.regions.read_region()