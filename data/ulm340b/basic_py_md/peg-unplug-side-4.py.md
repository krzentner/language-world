

and end your code with the text:

```
if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
    robot.grab("peg")
if check("the robot's gripper is forward aligned with the peg"):
    robot.unplug("peg")
if check("peg is not vertically aligned with the robot's gripper"):
    robot.drop("peg")
```

"""

# peg-unplug-side: grab the peg and pull the it out from the side
def peg_unplug_side(robot):
    # Check if peg is left of robot gripper
    if check("peg is left of the robot's gripper"):
        robot.move("gripper right")
    # Check if peg is forward aligned with robot gripper
    if check("peg is forward aligned with the robot's gripper"):
        robot.pull("peg out")
    if check("peg is not left of the robot's gripper and peg is not forward aligned with the robot's gripper"):
        robot.grab("peg")
    if check("the robot's gripper is forward aligned with the peg"):
        robot.unplug("peg")
    if check("peg is not vertically aligned with the robot's gripper"):
        robot.drop("peg")
[eod] [code]#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from unittest import mock

from trove.cluster.models import ClusterTasks
from trove.cluster.tasks import ClusterTasks as ClusterTasksClass
from trove.tests.unittests import trove_testtools


class ClusterTasksTest(trove_testtools.TestCase):

    @mock.patch('trove.cluster.models.LOG')
    def test_db_sync(self, mock_log):
        ct = ClusterTasksClass()
        ct.db_