

For example, you might start like this:

```
# window-close: slide the window closed to the right
def window_close(robot):
    # The robot's gripper is already below the window handle.
    # If the robot's gripper is not in front of the window handle, move the gripper to the left.
    # If the robot's gripper is in front of the window handle, push the window right.
    # If the robot's gripper is no longer in front of the window handle and there is no friction, push the window harder.
    if check("the robot's gripper is not in front of the window handle and there is friction"):
        robot.slide("the robot's gripper left")
    if check("the robot's gripper is in front of the window handle and there is friction"):
        robot.slide("the window to the right")
```
"""
__doc__ = f"{__doc__}\n\n{robot.window_close_docs}"

def window_close(robot):
    pass
[eod] [code]# -*- coding: utf-8 -*-

###############################################################################
#
# DescribeAlarmsForMetric
# Returns the specified alarms for the specified metric. Specify a statistic, period, or unit to filter the set of alarms further.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class DescribeAlarmsForMetric(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the DescribeAlarmsForMetric Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        Choreography.__init__(self, temboo_session, '/Library/Amazon/CloudWatch/DescribeAlarmsForMetric')


    def new_input_set(self):
        return DescribeAlarmsForMetricInputSet()

    def _make_result_set(self, result, path):
        return DescribeAlarmsForMetricResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return DescribeAlarmsForMetricChoreographyExecution(session, exec_id, path)

