# Steps:
    #  1. Pick up the stick 
    #  2. Move the stick towards the thermos
    #  3. Hook the stick around the handle of the thermos
    #  4. Drag the thermos to the target location
    # First, make sure the gripper is above the stick and close it to grab it.
    if check("the robot's gripper is not above the stick and the robot's gripper is open"):
        robot.move_gripper("above the stick", close_gripper=True)
    # Move the stick roughly above the thermos' handle.
    if check("the stick is not roughly above the thermos' handle"):
        robot.move_gripper("above the thermos' handle")
    # Hook the stick around the handle of the thermos.
    if check("the stick is not hooked around the handle of the thermos"):
        robot.move_gripper("around the handle of the thermos")
    # Move the thermos towards the destination
    if check("the thermos is not at the target location"):
        robot.move_gripper("near the target location")