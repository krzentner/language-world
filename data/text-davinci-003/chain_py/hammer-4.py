
    # Steps:
    #  1. Put gripper above nail
    #  2. Line up hammer
    #  3. Lower the hammer
    #  4. Hammer the nail
    # When hitting the nail, the hammer needs to be lined up with the nail before
    # it can be brought down effectively and hammer the nail.
    # First, move the gripper above the nail, so that we can line up the hammer.
    if check("the robot's gripper is not vertically aligned with nail"):
        robot.put("gripper above nail")
    # Once the gripper is above the nail, align the hammer with the nail.
    if check("the robot's gripper is above nail and the robot's gripper is around hammer"):
        robot.align("hammer to nail")
    # Once the hammer is lined up with the nail, lower the hammer to hit the nail.
    if check("the robot's gripper is aligned with the nail and the robot's gripper is below the nail"):
        robot.lower("hammer onto nail")
    # Once the hammer is at the nail, push the hammer down to hit the nail.
    if check("the robot's gripper is around hammer and the hammer is above nail"):
        robot.push("hammer down onto nail")