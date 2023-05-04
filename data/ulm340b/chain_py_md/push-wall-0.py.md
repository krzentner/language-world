

# MTurk Instructions

For each line of robot code, please select which instruction in the human program it refers to.
If you are not sure, you can select "Don't know".

Your choices will not affect your payment, since we will collect answers from many workers.
Please answer every question, even if you're not sure.

## Notes for Reviewers

We will first need to convert this data to the format used in our other studies.
Then, we will want to examine the effect that different programming
experiences have on workers' responses.

```
# door-open: pull the door open
def door_open(robot):
    # Steps:
    #  1. Put gripper above door handle
    #  2. Drop gripper around door handle
    #  3. Pull open the door
    # First, put the gripper mostly above the door handle.
    if check("the robot's gripper is not almost vertically aligned with door handle"):
        robot.put("gripper above door handle")
    # As long as the gripper is almost lined up, closing it should line it up
    # all the way.
    if check("the robot's gripper is almost vertically aligned with the door handle and the robot's gripper is open"):
        robot.put("gripper around door handle")
    # As long as the gripper is still vertically aligned with the door handle,
    # it's being opened, so keep pulling.
    if check("the robot's gripper is vertically aligned with the door handle"):
        robot.pull("door open")

# drawer-open: pull the drawer open
def drawer_open(robot):
    # Steps:
    #  1. Put gripper above drawer handle
    #  2. Drop gripper around drawer handle
    #  3. Pull open the drawer
    # We need to put the gripper above the drawer handle before we can grab it,
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with drawer handle"):
        robot.put("gripper above drawer handle")
    # Once the gripper is lined up above the drawer handle, we should be able to
    # grab the drawer handle by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with drawer handle and the robot's gripper is not around