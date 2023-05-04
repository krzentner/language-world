

and continue with a program that completes the task `pick-out-of-hole`, using
one or more of the following lines:

```
# This step uses the robot's sense of touch to find the top surface of the peg.
if check("the robot's gripper is not feeling the top of peg"):
    robot.align("robot's gripper to top surface of peg")

# This step uses the robot's sense of touch to find the top surface of the hole
if check("the robot's gripper is not feeling the top of hole"):
    robot.align("robot's gripper to top surface of hole")

# This step uses the robot's sense of touch to find the top surface of the hole
if check("the robot's gripper is not feeling the bottom of hole"):
    robot.align("robot's gripper to bottom surface of hole")

# This step uses the robot's sense of touch to find the left surface of the peg
if check("the robot's gripper is not feeling the left side of peg"):
    robot.align("robot's gripper to left surface of peg")

# This step uses the robot's sense of touch to find the right surface of the peg
if check("the robot's gripper is not feeling the right side of peg"):
    robot.align("robot's gripper to right surface of peg")

# This step uses the robot's sense of touch to find the left surface of the hole
if check("the robot's gripper is not feeling the left side of hole"):
    robot.align("robot's gripper to left surface of hole")

# This step uses the robot's sense of touch to find the right surface of the hole
if check("the robot's gripper is not feeling the right side of hole"):
    robot.align("robot's gripper to right surface of hole")

# This step uses the robot's sense of touch to find the inner surface of the hole
if check("the robot's gripper is not feeling the inner surface of hole"):
    robot.align("robot's gripper to inner surface of hole")

# This step uses the robot's sense of touch to find the outer surface of the hole
if check("the robot's gripper is not feeling the outer surface of hole"):
    robot.align("robot's gripper to outer surface of hole")
```

In each line above, replace each of the words "top", "left", "right",
"inner", and "outer