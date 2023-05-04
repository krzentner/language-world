

If you need help, the following words may be helpful:

```
robot
```

```
robot.move_gripper
```

```
robot.is_grasped
```

```
robot.open_gripper
```

```
robot.close_gripper
```

```
robot.is_open_gripper
```

```
robot.is_closed_gripper
```

```
robot.is_overhead_grasp
```

```
robot.is_around_grasp
```

```
robot.is_forward_grasp
```

```
check
```


'''

##################################################
#
# BUGGY CODE THAT NEEDS TO BE FIXED
#
##################################################
# # Steps:
#  1. Put gripper above wrench
#  2. Put gripper above peg
#  3. Grab peg
#  4. Wrap wrench around peg

# First, put the gripper above the wrench.
if check("the robot's gripper is not vertically aligned with wrench"):
    robot.move_gripper("vertically aligned with wrench")

# If the gripper is above the wrench, drop it around the wrench to grab it.
if check("the robot's gripper is vertically aligned with wrench"):
    robot.move_gripper("around the wrench")

# First, put the gripper above the peg.
if check("the robot's gripper is not vertically aligned with peg"):
    robot.move_gripper("vertically aligned with peg")

# If the gripper is above the peg, drop it around the peg to grab it.
if check("the robot's gripper is vertically aligned with peg"):
    robot.move_gripper("around the peg")

# First, put the gripper above the wrench.
if check("the robot's gripper is not vertically aligned with wrench"):
    robot.move_gripper("vertically aligned with wrench")

# If the gripper is above the wrench, drop it around the wrench to grab it.
if check("the robot's gripper is vertically aligned with wrench"):
    robot.move_gripper("around the wrench")

# First, put the gripper above the peg.
if check("the robot's gripper is not vertically aligned with peg"):
    robot.move_gripper("vertically aligned with peg")

# If the gripper is above the peg, drop it around the peg to grab it.
if check("the