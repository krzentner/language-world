

Steps:
  1. Put gripper above handle
  2. Move gripper around to the side
  3. Pull handle up

# handle-pull-side: pull up the handle from the side
# def handle_pull_side(robot):
    # Steps:
    #  1. Put gripper above handle
    #  2. Move gripper around to the side
    #  3. Pull handle up
    # First move the gripper above the handle.
    if check("the robot's gripper is not vertically aligned with the handle"):
        robot.put("gripper above handle")
    # Move the gripper around to the side of the handle.
    if check("the robot's gripper is vertically aligned with the handle and the robot's gripper is not to the side of the handle"):
        robot.move("gripper to side of handle")
    # Once the gripper is to the side of the handle, pull it up.
    if check("the robot's gripper is to the side of the handle"):
        robot.pull("handle up")