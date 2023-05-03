# stick-pull: grab the stick and use it to pull the thermos to the target location
def stick_pull(robot):
    # Steps:
    #  1. Put gripper above the stick
    #  2. Grab the stick with the gripper
    #  3. Line up the stick with the thermos handle
    #  4. Grab the thermos handle with the stick
    #  5. Drag the thermos towards the target location
    # First, put the gripper above the stick.
    if check("the robot's gripper is not vertically aligned with the stick"):
        robot.move_gripper("vertically aligned with the stick")
    # Once the gripper is aligned with the stick, close the gripper around it.
    if check("the robot's gripper is vertically aligned with the stick"):
        robot.move_gripper("around the stick")
    # Now that we have the stick, line it up with the thermos handle.
    if check("the robot's gripper is around the stick and the stick is not forward aligned with the thermos handle"):
        robot.move_gripper("forward aligned with the thermos handle")
    # Once the stick is lined up with the thermos handle, grab it.
    if check("the robot's gripper is forward aligned with the thermos handle"):
        robot.move_gripper("around the thermos handle")
    # Now that we have the thermos handle with the stick, we can drag it towards the target location.
    if check("the robot's gripper is around the thermos handle"):
        robot.move_gripper("near the target location")