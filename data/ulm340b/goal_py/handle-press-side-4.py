
    # Steps:
    #  1. Move the gripper in front of the handle
    #  2. Push down the handle
    # Move the robot's gripper in front of the handle.
    # Because the handle is a long object, check if the gripper is forward
    # aligned instead of around it.
    if check("the handle is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the handle")
    # If the handle is in front of the gripper, push it down.
    # Check if the handle is below the gripper instead of near it.
    if check("the handle is below the robot's gripper"):
        robot.move_gripper("near the handle", close_gripper=True)

# turn-lever-side: grip the lever and turn it from the side
def turn_lever_side(robot):
    # Steps:
    #  1. Put gripper above the lever
    #  2. Grab the lever with the gripper
    #  3. Turn the lever from the side
    # First, put the gripper above the lever.
    # Because the lever is a long object, check if the gripper is forward
    # aligned instead of around it.
    if check("the lever is not forward aligned with the robot's gripper"):
        robot.move_gripper("forward aligned with the lever")
    # If the lever is in front of the gripper, push it down.
    # Check if the lever is below the gripper instead of near it.
    if check("the lever is forward aligned with the robot's gripper"):
        robot.move_gripper("around the lever")
    # If the gripper is around the lever, we can turn the lever now by moving
    # the gripper left or right.
    if check("the robot's gripper is around the lever"):
        robot.move_gripper("almost vertically aligned with the lever")

# turn-lever-topdown: grip the lever and turn it from the top
def turn_lever_topdown(robot):
    # Steps:
    #  1. Put gripper above the lever
    #  2. Grab the lever with the gripper
    #  3. Turn the lever from the side
    # First, put the