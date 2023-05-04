

# Dialogue

In the previous experiment, we asked you to perform the first 11 tasks without any additional instructions to see how well you could figure out how to do them from the examples. In this experiment, we will instead give you more information about what to do. 

## Experimenter:

Here are some more instructions about how to do some of the tasks:

```
# drawer-close: push the drawer close
def drawer_close(robot):
    # Steps:
    #  1. Put gripper roughly around the drawer handle
    #  2. Push the drawer closed
    # Because the gripper is already roughly around the drawer handle, we
    # probably don't need to move the gripper more, just push the gripper back
    # and forth a little to see if we hit the drawer handle.
    if check("the robot's gripper is not near the drawer handle"):
        robot.grab("drawer handle")
    # If the drawer is aligned with the gripper as seen from in front, we can
    # push the drawer closed.
    if check("the robot's gripper is forward aligned with drawer handle"):
        robot.push("drawer closed")

# reach: reach to the target location
def reach(robot):
    # Steps:
    #  1. Reach towards the target
    # We don't have any objects to manipulate, so we can just move the robot's
    # gripper directly to the target location
    if check("the robot's gripper is not near reach target"):
        robot.reach("to goal")

# peg-insert-side: grab the peg and insert it into the hole from the side
def peg_insert_side(robot):
    # Steps:
    #  1. Put gripper above the peg
    #  2. Grab the peg with the gripper
    #  3. Line the peg up with the hole
    #  4. Slide the peg sideways into the hole
    # First, put the gripper above the peg.
    if check("the robot's gripper is not vertically aligned with the peg"):
        robot.put("gripper above peg")
    # If the peg becomes left of the gripper, go back to putting the gripper
    # above the peg.
    # Because the peg is a long object, check if the gripper is lined up with it
    # from