# Steps:
    #  1. Put gripper above the box lid
    #  2. Grab the box lid with the gripper
    #  3. Lift the box lid up
    #  4. Put gripper on top of the box
    #  5. Lower the box lid onto the box
    # First, put the gripper above the box lid.
    if check("the robot's gripper is not above the box lid"):
        robot.place("gripper above the box lid")
    # If the gripper is not around the box lid, grab the box lid.
    if check("the robot's gripper is not around the box lid" and "the robot's gripper is open"):
        robot.grab("the box lid")
    # If the gripper is around the box lid, lift it up.
    if check("the robot's gripper is around the box lid"):
        robot.lift("the box lid")
    # Place the gripper on top of the box.
    if check("the robot's gripper is not above the box"):
        robot.place("gripper on top of the box")
    # Lower the box lid onto the box.
    if check("the box lid is above the box"):
        robot.lower("the box lid onto the box")