

You can use the function `check` to check logical relationships
between objects on the table and the robot's gripper.

```
check("the robot's gripper is not above the puck")
```

You can use the function `robot.move_gripper` to move the robot's gripper
closer to the table.

```
robot.move_gripper("above the puck")
```

It is okay if the program is slightly repetitive; it is better to repeat
simple instructions than to combine things into a more complicated instruction.
If you find yourself getting confused, you might be trying to write too complicated of a
program.



"""

def plate_slide_back_side(robot):
    #Steps:
    #1. Line the robot's gripper up with the plate as viewed from the top.
    #2. Line up the robot's gripper with the target location as viewed from the side.
    #3. Push the plate into the target location.
    if check("the robot's gripper is not above the plate"):
        robot.move_gripper("above the plate")
    if check("the robot's gripper is not to the left of the target location"):
        robot.move_gripper("to the left of the target location")
    if check("the plate is not below the robot's gripper"):
        robot.move_gripper("almost touching the plate", close_gripper=True)

def button_press_topdown(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the button from the top
    # Because this is "topdown", we just need to line up the gripper from above.
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with button"):
        robot.move_gripper("vertically aligned with the button", close_gripper=True)
    # Now that the gripper is lined up, just push down on the button.
    if check("the robot's gripper is vertically aligned with button"):
        robot.move_gripper("near the button")

# drawer-open: pull the drawer open
def drawer_open(robot):
    # Steps:
    #  1. Put gripper above drawer handle
    #  2. Drop gripper around drawer handle
  