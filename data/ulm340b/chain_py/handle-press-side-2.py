
    # Steps:
    #  1. Line up the gripper as seen from above and in front
    #  2. Push down on the handle from the side
    # Because this is "side", we just need to line up the gripper from above and
    # in front.
    # Line up the robot's gripper from above.
    # Because the handle is a long object, check if the gripper is lined up with
    # it from in front as well.
    if check("the robot's gripper is not vertically aligned with handle and the robot's gripper is not forward aligned with handle"):
        robot.put("gripper above handle")
    # Now that the gripper is lined up, just push down on the handle from the
    # side.
    # Because the handle is a long object, check if the gripper is lined up with
    # it from in front as well.
    if check("the robot's gripper is vertically aligned with handle and the robot's gripper is forward aligned with handle"):
        robot.push("down on handle")

# handle-press-topdown: push down the handle from above
def handle_press_topdown(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the handle from above
    # Because this is "topdown", we just need to line up the gripper from above.
    # Line up the robot's gripper from above.
    if check("the robot's gripper is not vertically aligned with handle"):
        robot.put("gripper above handle")
    # Now that the gripper is lined up, just push down on the handle from above.
    if check("the robot's gripper is vertically aligned with handle"):
        robot.push("down on handle")

# handle-press-bottomup: push up the handle from below
def handle_press_bottomup(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above and in front
    #  2. Push up on the handle from below
    # Because this is "bottomup", we just need to line up the gripper from above
    # and in front.
    # Line up the robot's gripper from above.
    # Because the handle is a long object