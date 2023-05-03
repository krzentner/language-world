# Steps:
    #  1. Place gripper around lever handle
    #  2. Rotate gripper up
    # Lever pull is similar to drawer open. First, we need to put the gripper
    # roughly around the lever handle.
    if check("the robot's gripper is not mostly around lever handle"):
        robot.place("gripper around lever handle")
    # Once the gripper is around the lever handle, we can rotate the gripper up
    # to pull the lever.
    if check("the robot's gripper is around lever handle and the robot's gripper is not rotated up"):
        robot.rotate("gripper up")