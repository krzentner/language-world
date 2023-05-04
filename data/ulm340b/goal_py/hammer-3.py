
    # Steps:
    #  1. Put gripper above hammer
    #  2. Drop gripper around hammer
    #  3. Hit nail
    # If the hammer is not above the robot's gripper, move the gripper above the
    # hammer.
    if check("the robot's gripper is not above hammer"):
        robot.move_gripper("above the hammer", close_gripper=True)
    # Once the hammer is above the gripper, move the gripper around the hammer
    # to pick it up.
    if check("the robot's gripper is above hammer"):
        robot.move_gripper("around the hammer")
    # Once the robot's gripper is around the hammer, just hit the nail by moving
    # the gripper down.
    if check("the robot's gripper is around hammer"):
        robot.move_gripper("vertically aligned with the nail")

# sweep: clean the surface of the table
def sweep(robot):
    # Steps:
    #  1. Put gripper above broom
    #  2. Drop gripper around broom
    #  3. Pick up broom
    #  4. Sweep table
    # Because the broom is not a round object, we need to drop the gripper
    # around the broom before we can lift it.
    # If the broom is above the robot's gripper, move the gripper above the
    # broom.
    if check("the robot's gripper is not above broom"):
        robot.move_gripper("above the broom", close_gripper=True)
    # Once the broom is above the gripper, move the gripper around the broom to
    # pick it up.
    if check("the robot's gripper is not around broom"):
        robot.move_gripper("around the broom")
    # Once the robot's gripper is around the broom, we can pick it up and start
    # sweeping.
    if check("the robot's gripper is around broom"):
        robot.move_gripper("around the broom")

# pour: pour water from the kettle into the cup
def pour(robot):
    # Steps:
    #  1. Put gripper above the handle of the kettle
    #  