
    # Steps:
    #  1. Put the robot's gripper above the hammer
    #  2. Drop the gripper around the hammer
    #  3. Close the gripper around the hammer
    #  4. Move the hammer to the nail
    #  5. Hit the nail with the hammer
    # First, put the gripper above the hammer.
    if check("the robot's gripper is not above the hammer"):
        robot.put("gripper above hammer")
    # If the gripper is above the hammer, grab it by dropping the gripper around
    # the hammer.
    if check("the robot's gripper is above the hammer and the robot's gripper is open"):
        robot.drop("gripper around hammer")
    # Once the gripper is around the hammer, we should close the gripper to make
    # sure we have a good grip.
    if check("the robot's gripper is around the hammer and the robot's gripper is open"):
        robot.close("gripper around hammer")
    # If the hammer is held in the gripper, we can move it to the nail.
    if check("the robot's gripper is around the hammer and the robot's gripper is closed"):
        robot.move("hammer to nail")
    # Once the hammer is over the nail, hit the nail.
    if check("the hammer is over the nail"):
        robot.hit("nail with hammer")