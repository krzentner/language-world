
    # Steps:
    #  1. Put gripper above handle
    #  2. Drop gripper around handle
    #  3. Pull up handle
    # Put the robot's gripper above the handle so that the gripper's angle
    # works.
    if check("the robot's gripper is not above handle"):
        robot.move_gripper("vertically aligned with the handle")
    # Move the gripper down around the handle to grab it.
    if check("the robot's gripper is above handle and the robot's gripper is not around handle"):
        robot.move_gripper("around handle")
    # Pull up on the handle to operate it.
    if check("the robot's gripper is around handle"):
        robot.move_gripper("left of handle")

# handle-push: push down the handle
def handle_push(robot):
    # Steps:
    #  1. Put gripper above handle
    #  2. Drop gripper around handle
    #  3. Push down handle
    # Put the robot's gripper above the handle so that the gripper's angle
    # works.
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.move_gripper("vertically aligned with the handle")
    # Move the gripper down around the handle to grab it.
    if check("the robot's gripper is vertically aligned with handle and the robot's gripper is not around handle"):
        robot.move_gripper("around handle")
    # Push down on the handle to operate it.
    if check("the robot's gripper is around handle"):
        robot.move_gripper("above handle")

# switch-press: push the switch down
def switch_press(robot):
    # Steps:
    #  1. Put gripper above switch
    #  2. Push switch down
    # Move the gripper above the switch.
    if check("the robot's gripper is not vertically aligned with switch"):
        robot.move_gripper("vertically aligned with the switch")
    # Push the switch down.
    if check("the robot's gripper is vertically aligned with switch"):
        robot.move_gripper("above the switch")

#