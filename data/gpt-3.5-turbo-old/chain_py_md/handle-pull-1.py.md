# handle-pull: pull up the handle
# def handle_pull(robot):
    # Steps:
    #  1. Put gripper above the handle
    #  2. Grab the handle
    #  3. Pull up the handle
    # First put the gripper above the handle
    if check("the robot's gripper is not above the handle"):
        robot.place("gripper above handle")
    # Once the gripper is above the handle we should be able to grab the handle by moving the gripper down
    if check("the robot's gripper is above the handle and the robot's gripper is not around handle"):
        robot.drop("gripper around handle")
    # Once the gripper is around the handle we can pull the handle up
    if check("the robot's gripper is around handle"):
        robot.pull("up on handle")