

Here's the code for lever-pull:

```
# lever-pull: rotate the lever up
def lever_pull(robot):
    # Steps:
    #  1. Put gripper above the lever
    #  2. Drop gripper around the lever 
    #  3. Rotate the lever clockwise
    # First, put the gripper roughly above lever, so that we don't bump it while
    # trying to grab it. 
    if check("the robot's gripper is not above the lever"):
        robot.move_gripper("above the lever")
    # If the gripper isn't around the lever, put it around the lever.
    if check("the robot's gripper is not around lever and the robot's gripper is open"):
        robot.move_gripper("near the lever", close_gripper=True)
    # If the gripper is near the lever and open, maybe we can grab it by closing
    # the gripper.
    if check("the robot's gripper is above the lever and the robot's gripper is closed"):
        robot.move_gripper("nearest the upper part of the lever")
    # Rotate the lever.
    if check("the robot's gripper is around the lever"):
        robot.move_gripper("clockwise around the lever")
``