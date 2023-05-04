
    # Steps:
    #  1. Put gripper above the wrench
    #  2. Grab the wrench with the gripper
    #  3. Move the wrench off the peg
    #  4. Put the wrench near the goal
    # First, put the gripper above the wrench.
    if check("the robot's gripper is not vertically aligned with the wrench"):
        robot.move_gripper("vertically aligned with the wrench")
    # If the wrench becomes right of the gripper, go back to putting the gripper
    # above the wrench.
    # Because the wrench is a long object, check if the gripper is lined up with
    # it from the front instead of around it.
    if check("the wrench is not right of the robot's gripper and the wrench is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the wrench", close_gripper=True)
    # As long the gripper is still mostly around the wrench and the wrench isn't
    # near the goal, move the wrench to the goal.
    if check("the wrench is around the robot's gripper and the wrench is not near the goal"):
        robot.move_gripper("horizontally aligned with goal")

# door-close: push the door closed
def door_close(robot):
    # Steps:
    #  1. Put gripper above door handle
    #  2. Drop gripper around door handle
    #  3. Push the door closed
    # We need to put the gripper above the door handle before we can grab it,
    # because of the angle of the robot's gripper.
    if check("the robot's gripper is not vertically aligned with door handle"):
        robot.move_gripper("vertically aligned with the door handle")
    # Once the gripper is lined up above the door handle, we should be able to
    # grab the door handle by moving the gripper down around it.
    if check("the robot's gripper is vertically aligned with door handle and the robot's gripper is not around door handle"):
        robot.move_gripper("around the door handle")
    # Once the gripper is around the door handle, we can just push the door
    # closed.
    if check("the robot's gripper