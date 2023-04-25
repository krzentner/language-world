

# door-close: push the door closed to the target location
# def door_close(robot):
    # Steps:
    #  1. Put gripper left of the door handle
    #  2. Push the door closed
    # First, put the gripper to the left of the door handle so that it can be used to push the door closed.
    if check("the robot's gripper is not left of the door handle"):
        robot.move_gripper("left of the door handle")
    # Once the gripper is in position, push the door closed.
    if check("the robot's gripper is left of the door handle"):
        robot.move_gripper("around the door handle")