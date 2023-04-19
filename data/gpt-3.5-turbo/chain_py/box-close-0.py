# Steps:
    #  1. Put gripper above box lid
    #  2. Grab box lid with the gripper
    #  3. Lift the box lid off the box
    #  4. Move the gripper above the box
    #  5. Lower the box lid onto the box
    # First, put the gripper above the box lid.
    if check("the robot's gripper is not above the box lid"):
        robot.place("gripper above box lid")
    # If the gripper is above the box lid, grab it with the gripper.
    if check("the robot's gripper is above the box lid and the robot's gripper is open"):
        robot.grab("box lid")
    # Once the box lid is grabbed, lift it off the box.
    if check("the box lid is grabbed by the gripper"):
        robot.lift("box lid off the box")
    # Move the gripper above the box.
    if check("the robot's gripper is not above the box"):
        robot.place("gripper above box")
    # Lower the box lid onto the box.
    if check("the robot's gripper is above the box and the box lid is grabbed by the gripper"):
        robot.lower("box lid onto the box")