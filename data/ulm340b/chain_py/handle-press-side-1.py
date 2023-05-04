
    # Steps:
    #  1. Align the gripper from in front of the handle
    #  2. Push the handle down
    # Because this is "side", we just need to line up the gripper from in front.
    # Line up the robot's gripper from in front.
    if check("the robot's gripper is not forward aligned with handle"):
        robot.put("gripper near the handle")
    # Now that the gripper is lined up, just push the handle down.
    if check("the robot's gripper is forward aligned with handle"):
        robot.push("the handle down")

# handle-press-topdown: push down the handle from above
def handle_press_topdown(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the handle from the top
    # Because this is "topdown", we just need to line up the gripper from above.
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.put("gripper above handle")
    # Now that the gripper is lined up, just push the handle down.
    if check("the robot's gripper is vertically aligned with handle"):
        robot.push("the handle down")

# handle-pull-side: pull up the handle from the side
def handle_pull_side(robot):
    # Steps:
    #  1. Align the gripper from in front of the handle
    #  2. Pull the handle up
    # Because this is "side", we just need to line up the gripper from in front.
    # Line up the robot's gripper from in front.
    if check("the robot's gripper is not forward aligned with handle"):
        robot.put("gripper near the handle")
    # Now that the gripper is lined up, just pull the handle up.
    if check("the robot's gripper is forward aligned with handle"):
        robot.pull("the handle up")

# handle-pull-topdown: pull up the handle from above
def handle_pull_topdown(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above
  