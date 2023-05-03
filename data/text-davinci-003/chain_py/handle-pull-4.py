
    # Steps:
    #  1. Put gripper around handle
    #  2. Pull up on handle
    # To pull the handle, we first need to wrap the gripper around it
    if check("the robot's gripper is not around the handle"):
        robot.put("gripper around handle")
    # If the gripper is lined up with the handle, we can just pull it up
    # directly.
    if check("the robot's gripper is around the handle"):
        robot.pull("up on handle")

# edge-push-hold: hold the object with the robot's edge
def edge_push_hold(robot):
    # Steps:
    #  1. Put robot to the side of the object
    #  2. Wrap robot's edge into object
    #  3. Press the edge against the object
    #  4. Hold the object
    # First, move the robot to the side of the object
    if check("robot is not near object"):
        robot.put("robot to side of object")
    # If the robot's edge is against the object but its gripper isn't wrapped
    # around it, pull the gripper around it.
    # We don't want to do this too quickly, since the gripper may overshoot and
    # slide down the object.
    if check("robot's gripper is not around object"):
        robot.wrap("robot's edge into object")
    # If the gripper is around the object and the robot's edge isn't pressing
    # down on it, press the edge onto the object.
    if check("robot's gripper is around object and robot's edge is not against object"):
        robot.press("edge onto object")
    # As long as the robot's gripper and edge are wrapping around the object,
    # it should be held.
    # If it's not held and the above conditions fail, we must move back to an
    # earlier step.
    if check("robot's gripper is around object and robot's edge is against object"):
        robot.grab("object")