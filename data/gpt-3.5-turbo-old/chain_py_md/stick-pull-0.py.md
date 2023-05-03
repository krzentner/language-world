# stick-pull: use the stick to pull the thermos to the target location
# def stick_pull(robot):
    # Steps:
    #  1. Put gripper above the stick
    #  2. Grab the stick with the gripper
    #  3. Move the end of the stick into contact with the thermos handle
    #  4. Wrap the gripper around the thermos handle
    #  5. Lift the thermos off the surface
    #  6. Move the thermos to the target location
    #  7. Put the thermos down
    # First, put the gripper above the stick.
    if check("the robot's gripper is not vertically aligned with the stick"):
        robot.put("gripper above the stick")
    # Next, grab the stick with the gripper.
    if check("the robot's gripper is not around the stick"):
        robot.grab("the stick")
    # Move the end of the stick into contact with the thermos handle.
    if check("the end of the stick is not in contact with the thermos handle"):
        robot.move("the end of the stick towards the thermos handle")
    # Wrap the gripper around the thermos handle.
    if check("the robot's gripper is not around the thermos handle"):
        robot.wrap("the gripper around the thermos handle")
    # Lift the thermos off the surface.
    if check("the thermos is not lifted off the surface"):
        robot.lift("the thermos off the surface")
    # Move the thermos to the target location.
    if check("the thermos is not at the target location"):
        robot.move("the thermos to the target location")
    # Put the thermos down at the target location.
    if check("the thermos is not on the target location"):
        robot.put("the thermos down")