# handle-pull-side: pull up the handle from the side
# def handle_pull_side(robot):
    # Steps:
    #  1. Put gripper next to handle on the side
    #  2. Grab handle with the gripper
    #  3. Pull the handle upwards
    # We need to put the gripper next to the handle on the side.
    if check("the robot's gripper is not next to the handle on the side"):
        robot.move("the gripper next to the handle on the side")
    # If the gripper is next to the handle on the side, we need to grab it.
    if check("the robot's gripper is next to the handle on the side and the gripper is not around the handle"):
        robot.grab("the handle with the gripper")
    # Finally, pull up on the handle.
    if check("the gripper is around the handle"):
        robot.pull_up("on the handle")