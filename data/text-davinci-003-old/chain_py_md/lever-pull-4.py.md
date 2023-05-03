

Then, add the necessary code:

```
# lever-pull: rotate the lever up
# def lever_pull(robot):
    # Steps:
    #  1. Put the gripper on the side of the lever
    #  2. Close the gripper around the lever
    #  3. Pull the lever up
    # We need to put the gripper to the side of the lever to make sure that it
    # grabs the lever securely. 
    if check("the robot's gripper is not sideways aligned with lever"):
        robot.put("gripper to side of lever")
    # Now that the gripper is at the side of the lever, close it around the lever.
    if check("the robot's gripper is sideways aligned with lever and the gripper is open"):
        robot.close("gripper around lever")
    # Now that the gripper is closed around the lever, try to pull the lever up.
    if check("the robot's gripper is close to the lever and closed"):
        robot.pull("lever up")
``