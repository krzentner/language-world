
    # Steps:
    #  1. Move gripper to top of nail
    #  2. Move hammer back
    #  3. Hit the nail
    # First, put the gripper on top of the nail to stabilize the nail.
    if check("the robot's gripper is not above the nail"):
        robot.move("gripper to top of nail")
    # Once the gripper is above the nail, move the hammer backwards.
    if check("the robot's gripper is above the nail"):
        robot.pull("hammer back")
    # Now hit the nail with the hammer.
    if check("the robot's gripper is above the nail and the hammer is pulled back"):
        robot.hit("the nail")

# plug-side: insert the plug into the outlet from the side
def plug_side(robot):
    # Steps:
    #  1. Put gripper above the plug
    #  2. Grab the plug
    #  3. Align the plug to the outlet
    #  4. Insert the plug into the outlet
    # First, we put the gripper above the plug.
    if check("the robot's gripper is not vertically aligned with the plug"):
        robot.put("gripper above plug")
    # If the plug is not aligned with the gripper as seen from in front, try
    # moving the gripper around the plug.
    if check("plug is not forward aligned with the robot's gripper and plug is not left of the robot's gripper"):
        robot.grab("plug")
    # If the gripper is around the plug and the plug is not aligned with the
    # outlet, align the plug with the outlet.
    if check("the robot's gripper is forward aligned with the plug and the plug is not horizontally aligned with the outlet"):
        robot.align("plug with the outlet")
    # If the plug is lined up with the outlet to the side, insert it.
    if check("plug is horizontally aligned with outlet"):
        robot.insert("plug into outlet")

# plug-topdown: insert the plug into the outlet from above
def plug_topdown(robot):
    # Steps:
    #  1. Line up the gripper as viewed from above
    #  2. Push down on the plug
   