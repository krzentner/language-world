

And then follow with a program that follows these steps:

```
# Steps:
#  1. Put gripper above cube
#  2. Grab cube
#  3. Slide cube sideways to target
# First, line up the gripper above cube
if check("the robot's gripper is not vertically aligned with the cube and the robot's gripper is not near the cube"):
    robot.put("gripper above cube")
# As long as the gripper is lined up above cube, it's safe to just grab the
# cube.
if check("the robot's gripper is vertically aligned with cube"):
    robot.put("gripper around cube")
# Once the gripper is around cube, we can just slide it to the goal.
if check("the robot's gripper is near the cube and the robot's gripper is vertically aligned with the cube"):
    robot.move("cube sideways to the goal")
```

## What would you say to me if I asked you: "Can you use the robot to get the button pressed?"

The robot can push the button using the program `button-press-topdown`.

## What would you say to me if I asked you: "Can you use the robot to sweep the cube to the target location?"

The robot can sweep the cube to the target location using the program `sweep`.

'''[eod] [code]'''
@Author: Yingshi Chen

@Date: 2019-09-14 10:49:47
@
# Description: 
'''
import torch
import torch.nn as nn
import torch.nn.functional as F
from ..model_utils import (swish,
                           gelu,
                           )


class Attention(nn.Module):
    def __init__(self,
                 dim,
                 d_k,
                 hidden_size,
                 dropout=0.1,
                 use_selu=False,
                 use_mha=False,
                 ):
        super(Attention, self).__init__()
        self.hidden_size = hidden_size
        self.d_k = d_k
        self.linears = nn.ModuleList([nn.Linear(dim, d_k),
                                      nn.Linear(dim, d_k),
                                      ])
        self.use_selu = use_selu
        if self.use_selu:
            self.non_linearity = torch.nn.SELU()
        else:
            self.non_linearity = 