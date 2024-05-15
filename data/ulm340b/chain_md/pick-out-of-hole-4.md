
    First, put the gripper roughly above peg, so that we don't bump it while trying to grab it.
    - When the robot's gripper is not vertically aligned with the peg, the robot should move gripper above peg.
    The peg is below the gripper, so we've probably picked it up, so try to put it at the target location.
    - When the peg is vertically aligned with the robot's gripper, the robot should move peg to target.
    """
[eod] [code]from ..factory import Type


class updateOption(Type):
	option = None  # type: "Option"
	description = None  # type: "string"
[eod] [code]#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_geonames
----------------------------------

Tests for `geonames` module.
"""


import sys
import unittest
from click.testing import CliRunner

from geonames import geonames
from geonames import cli



class TestGeonames(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_something(self):
        pass

    def test_command_line_interface(self):
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'geonames.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
[eod] [code]# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-29 02:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_group_group_leader'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='group_leader',
            field=models.ForeignKey(default=1, on_delete=models.CASCADE, related_name='leaders', to='auth.User'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group'