
    # Steps:
    #  1. Move gripper to left of handle
    #  2. Move gripper towards the handle
    #  3. Push down on the handle
    # The handle is probably initially right of the robot's gripper, so move the
    # gripper to the left of the handle.
    if check("the robot's gripper is not forward aligned with handle and the robot's gripper is not left of handle"):
        robot.move("gripper to left of handle")
    # As long as the handle isn't directly left of the gripper and not near the
    # gripper, move the gripper towards the handle.
    # Because the handle is a long object, check if the gripper is lined up with
    # it from the front instead of around it.
    if check("handle is not left of the robot's gripper and handle is not forward aligned with the robot's gripper"):
        robot.grab("handle")
    # If the gripper is aligned with the handle as seen from in front, push the
    # handle down.
    if check("the robot's gripper is forward aligned with handle"):
        robot.push("handle down")

# handle-pull-side: pull up the handle from the side
def handle_pull_side(robot):
    # Steps:
    #  1. Move gripper to left of handle
    #  2. Grab handle with the gripper
    #  3. Pull handle upwards
    # The handle is probably initially right of the robot's gripper, so move the
    # gripper to the left of the handle.
    if check("the robot's gripper is not forward aligned with handle and the robot's gripper is not left of handle"):
        robot.move("gripper to left of handle")
    # As long as the handle isn't directly left of the gripper, grab the
    # handle.
    # Because the handle is a long object, check if the gripper is lined up with
    # it from the front instead of around it.
    if check("handle is not left of the robot's gripper and handle is not forward aligned with the robot's gripper"):
        robot.grab("handle")
    # If the gripper is aligned with the handle as seen from in front, pull it
    #