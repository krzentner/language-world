

We would like to see a sequence of English commands to the robot, interspersed with checks to see whether the desired state has been achieved.

### Task ###

Use the following instructions to write the code for the task `peg_insert_side` above.

1. Read through all of the examples of tasks for other robots to get an idea of what commands and checks can be used.

2. Think about how you might do the task `peg_insert_side` yourself if you were the robot. Write out in English the sequence of actions that you think you would need to do.

3. Now write out the actions in code, by translating each English instruction into a command to the robot.

```
# peg-insert-side: grab the peg and insert it into the hole from the side
def peg_insert_side(robot):
```

```
# door-open: pull the door open
def door_open(robot):
    # Steps:
    #  1. Put gripper above door handle
    #  2. Drop gripper around door handle
    #  3. Pull open the door
    # First, put the gripper mostly above the door handle.
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.move_gripper("almost vertically aligned with the door handle", close_gripper=True)
    # As long as the gripper is almost lined up, closing it should line it up
    # all the way.
    if check("the robot's gripper is vertically aligned with the door handle"):
        robot.move_gripper("left of the door handle")

# drawer-open: pull the drawer open
def drawer_open(robot):
    # Steps:
    #  1. Put gripper above drawer handle
    #  2. Drop gripper around drawer handle
    #  3. Pull open the drawer
    # We need to put the gripper above the drawer handle before we can grab it,
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.move_gripper("vertically aligned with the drawer handle")
    # Once the gripper is lined up above the drawer handle, we should be able to
    # grab the drawer handle by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with drawer handle and the robot's