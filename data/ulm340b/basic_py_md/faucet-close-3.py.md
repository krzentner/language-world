

For this program you will need to use the command:
robot.turn("right")
'''


def faucet_close(robot):
    if check("the robot's gripper is below the faucet"):
        robot.move("gripper to right of the faucet")
    if check("the robot's gripper is not in front of the faucet"):
        robot.grab("the faucet")
    if check("the robot's gripper is in front of the faucet"):
        robot.turn("right")


print faucet_close
[eod] [code]#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `a_b_c` package."""

import pytest

from click.testing import CliRunner

from a_b_c import a_b_c
from a_b_c import cli


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'a_b_c.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
[eod] [code]#!/usr/bin/python
#
#  Copyright 2002-2018 Barcelona Supercomputing Center (www.bsc.es)
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed