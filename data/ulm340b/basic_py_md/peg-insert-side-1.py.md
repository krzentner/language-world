

Please do not use any functions from the code examples above, even if they seem very similar to one of the examples (this makes the autograder happy).

"""
# The answer to this is probably
#    if check("the robot's gripper is not vertically aligned with peg"):
#        robot.put("gripper above peg")
#    if check("the robot's gripper is vertically aligned with peg and the robot's gripper is open"):
#        robot.put("gripper around peg")
#    if check("the robot's gripper is around peg and the robot's gripper is open"):
#        robot.close("gripper around peg")
#    if check("the robot's gripper is vertically aligned with peg and the robot's gripper is closed"):
#        robot.insert("peg into hole from side")
#    if check("the robot's gripper is horizontally aligned with hole"):
#        robot.place("gripper above hole")
#    if check("the robot's gripper is above hole and the robot's gripper is open"):
#        robot.drop("gripper")
[eod] [code]import json
from abc import ABCMeta, abstractmethod


class JsonDecoder(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def decode(self, json_data):
        raise NotImplementedError()

    def dump(self, json_data):
        return json.dumps(json_data, indent=4, sort_keys=True)


class JsonObjectDecoder(JsonDecoder):
    def __init__(self):
        self.json_object = {}

    def decode(self, json_data):
        self.json_object = json.loads(json_data)

    def get_data(self):
        return self.json_object
[eod] [code]#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "openmotif-%s" % get.srcVERSION()


def setup():
    shelltools.chmod("Imakefile", 0644)

    auto