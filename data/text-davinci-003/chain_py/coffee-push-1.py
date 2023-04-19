
    # Steps:
    #  1. Put gripper close to mug handle
    #  2. Grab mug from handle and lift it slightly
    #  3. Push the mug to the target location
    # If the robot's gripper isn't near the mug handle, it should move the
    # gripper near the handle.
    if check("the robot's gripper is not near the mug handle"):
        robot.place("gripper at the mug handle")
    # Once the robot's gripper is near the handle and the mug is lower than the
    # gripper, the robot can grab the mug handle.
    if check("the robot's gripper is near the mug handle and the mug is below the robot's gripper"):
        robot.grab("mug from handle")
    # Now the robot needs to lift the mug and move it to the target location.
    if check("the mug is above the robot's gripper"):
        robot.push("tuug to the target location")