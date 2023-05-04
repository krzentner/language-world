
    # Steps:
    #  1. Put gripper around the wrench
    #  2. Grab the wrench by moving the gripper up
    #  3. Put gripper around the peg
    #  4. Let go of the wrench to wrap it around the peg
    # Start by putting the gripper above the wrench.
    if check("the robot's gripper is not vertically aligned with wrench"):
        robot.put("gripper above the wrench")
    # Put the gripper around the wrench by moving it forward.
    if check("the robot's gripper is vertically aligned with the wrench and the wrench is not around the robot's gripper"):
        robot.grab("the wrench")
    # Put the gripper around the peg.
    if check("the robot's gripper is forward aligned with the wrench and the peg is not around the robot's gripper"):
        robot.grab("the peg")
    # Release the gripper around the peg so the wrench wraps around the peg.
    if check("the robot's gripper is forward aligned with the wrench"):
        robot.release("gripper")

# plug-insert: insert a plug into a hole
def plug_insert(robot):
    # Steps:
    #  1. Put gripper above the plug
    #  2. Grab the plug with the gripper
    #  3. Line the plug up with the hole
    #  4. Insert the plug into the hole
    # First, put the gripper above the plug.
    if check("the robot's gripper is not vertically aligned with the plug"):
        robot.put("gripper above plug")
    # If the plug becomes right of the gripper, go back to putting the gripper
    # above the plug.
    # Because the plug is a long object, check if the gripper is lined up with it
    # from the front instead of around it.
    if check("plug is not right of the robot's gripper and the plug is not forward aligned with the robot's gripper"):
        robot.grab("the plug")
    # As long the gripper is still mostly around the plug and the plug isn't lined
    # up with the hole, line up the plug with the hole.
    if check("the robot's gripper is forward aligned with the plug and the plug is not