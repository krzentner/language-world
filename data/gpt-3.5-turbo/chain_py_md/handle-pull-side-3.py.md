# handle-pull-side: pull up the handle from the side
def handle_pull_side(robot):
    # Steps:
    #   1. Move the gripper to the left of the handle
    #   2. Grab the handle
    #   3. Lift the handle up
    #   4. Move the gripper to the right of the handle
    # First, move the gripper to the left of the handle.
    if check("the robot's gripper is not left of the handle"):
        robot.move("gripper to left of handle")
    # If the gripper is left of the handle, grab it.
    if check("the robot's gripper is left of the handle and the robot's gripper is not around the handle"):
        robot.grab("handle")
    # Once the gripper is around the handle, lift the handle up vertically.
    if check("the robot's gripper is around the handle and the handle is not lifted up"):
        robot.lift("handle")
    # Once the handle is lifted up, move the gripper to the right of the handle so
    # that we can easily move it to a new location.
    if check("the handle is lifted up and the robot's gripper is not right of the handle"):
        robot.move("gripper to right of handle")