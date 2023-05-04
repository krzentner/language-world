
Steps:  1. Put the gripper above the cube  2. Grab the cube with the gripper  3. Move the cube to the target bin and place it inside
First, put the gripper above the cube.
    - When the robot's gripper is not above the cube, move the robot's gripper until the robot's gripper is above the cube
As long the gripper is above the cube and the gripper is not around the cube, close the gripper around the cube.
    - When the robot's gripper is not around the cube and the robot's gripper is open, move the robot's gripper until the robot's gripper is near the cube and the robot's gripper is closed
As long the gripper is closed and the cube is below the gripper, move the cube to the target bin and place it inside.
    - When the robot's gripper is around the cube and the cube is below the robot's gripper, move the robot's gripper until the robot's gripper is horizontally aligned with the target bin
""")[eod] [code]#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.
#
import copy

import mock
import testtools

from openstackclient.common import exceptions
from openstackclient.common import utils
from openstackclient.identity.v2_0 import user
from openstackclient.identity.v2_0 import user_role
from openstackclient.identity.v3 import user_role
from openstackclient.tests.identity.v2_0 import fakes as identity_fakes


class TestUserRole(identity_fakes.TestIdentityv2):

    def setUp(self):
        super(TestUserRole, self).setUp()

        # Get a shortcut to the UserManager Mock
        self.users_mock = self.app.client_manager.identity.users
        self.users_mock.reset_mock()

        # Get a shortcut to the UserRoleManager Mock
        self.users_role_mock = self.app.client_