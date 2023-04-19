# Steps:
    #  1. Put the gripper near the mug
    #  2. Open the gripper
    #  3. Grab the mug by closing the gripper around its handle
    #  4. Lift the mug up by moving the gripper upwards
    #  5. Move the mug to the target location
    #  6. Place the mug down by opening the gripper
    # First, put the gripper near the mug:
    if check("the robot's gripper is not near the mug"):
        robot.put("gripper near the mug")
    # If the gripper is near the mug but not open, open it:
    if check("the robot's gripper is near the mug and not open"):
        robot.drop("gripper open")
    # If the gripper is open but not around the mug's handle, close it around
    # the handle:
    if check("the robot's gripper is open and not around mug's handle"):
        robot.close("gripper around mug's handle")
    # If the gripper is closed around the handle, lift the mug up by moving the
    # gripper upwards:
    if check("the robot's gripper is around the mug's handle" and "the mug is not lifted up"):
        robot.lift("the mug up")
    # If the mug is lifted up and not near the target location, move it to the
    # target location:
    if check("the mug is lifted up and not near the target location"):
        robot.move("the mug to the target location")
    # If the mug is near the target location, place it down by opening the
    # gripper:
    if check("the mug is near the target location"):
        robot.drop("gripper open")