# Steps:
    #  1. Put gripper above stick
    #  2. Grab stick with gripper
    #  3. Line up stick with thermos handle
    #  4. Use stick to pull the thermos to the target location
    # First, put the gripper above the stick.
    if check("the robot's gripper is not almost vertically aligned with the stick"):
        robot.move_gripper("almost vertically aligned with the stick")
    # If the stick isn't below the gripper, move the gripper above the stick.
    if check("the stick is not below the robot's gripper and the stick is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the stick")
    # Once the gripper is above the stick, grab it with the gripper.
    if check("the stick is below the robot's gripper and the robot's gripper is open"):
        robot.move_gripper("around the stick")
    # Once the gripper is around the stick, we can move it to the thermos handle.
    if check("the robot's gripper is around the stick and the robot's gripper is not forward aligned with thermos handle"):
        robot.move_gripper("forward aligned with the thermos handle")
    # Once the gripper is around the thermos handle, use the stick to pull the thermos to the target location.
    if check("the robot's gripper is around the thermos handle"):
        robot.move_gripper("above the target location")