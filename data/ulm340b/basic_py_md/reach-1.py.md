

and follow the programming style of the previous tasks.
To complete the `reach` task, the robot should:

- move the gripper above the target location
- if the target location is behind a window, close it
- if the target location is inside a drawer, open it
- push the target location

For example, if the target location is behind a window:

```
# reach: reach to the target location
def reach(robot):
    if check("the robot's gripper is not vertically aligned with the target"):
        robot.put("the gripper above the target")
    if check("the target is behind the window and the window is open"):
        robot.window_close()
    if check("the target is behind the window"):
        robot.push("the target location")
```

If the target location is inside a drawer:

```
# reach: reach to the target location
def reach(robot):
    if check("the robot's gripper is not vertically aligned with the target"):
        robot.put("the gripper above the target")
    if check("the target is inside the drawer and the drawer is closed"):
        robot.drawer_open()
    if check("the target is inside the drawer"):
        robot.push("the target location")
```

'''
[eod] [code]# https://leetcode.com/problems/maximum-subarray/

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ending = max_all = nums[0]
        for i in range(1, len(nums)):
            max_ending = max(nums[i], max_ending + nums[i])
            max_all = max(max_ending, max_all)
        return max_all
[eod] [code]# -*- coding: utf-8 -*-
from openerp import models, api, fields, exceptions
from datetime import datetime, timedelta


class HrPayslip(models.Model):
    _inherit = "hr.payslip"

    has_reimbursement = fields.Boolean("Has Reimbursement", default=False)

    @api.model
    def get_inputs(self, contracts, date_from, date_to):
        self.ensure_one()
        if contracts:
            res = super(HrPayslip, self).get_inputs(contracts, date_from,
                    date_to)
        else:
            res = []