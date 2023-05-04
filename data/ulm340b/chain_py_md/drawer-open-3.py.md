

"""

__solution = """
# drawer-open: pull the drawer open
def drawer_open(robot):
    # Steps:
    #  1. Put gripper roughly around the drawer handle
    #  2. Pull the drawer open
    # If the gripper is not near the drawer handle, move it to the drawer
    # handle.
    # We don't need to be careful about the direction, since the drawer is large
    # and we're just pushing it (unlike when opening the drawer).
    if check("the robot's gripper is not near the drawer handle"):
        robot.grab("drawer handle")
    # If the drawer is aligned with the gripper as seen from in front, we can
    # pull the drawer open.
    if check("the robot's gripper is forward aligned with the drawer handle"):
        robot.pull("drawer open")
"""
[eod] [code]# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""Component tests for VMs command"""

from typing import Dict

from ..default_cmds import VirtualMachines
from .component_test import ComponentTest


class TestComponentVirtualMachines(ComponentTest):
    """Test class for VirtualMachines command"""

    def test_vms_list(self, server: Dict[str, str], cloud_provider: str) -> None:
        command: VirtualMachines = self.prepare_for_command(VirtualMachines, cloud_provider)

        self.assertEqual(command.name, "vms")
        self.assert_manager(command.manager, cloud_provider)

        # execute cmd
        command.execute()

        # validate terraform template
        template_string = self.get_template_string()
        self.assertIn