# box-close: pick up the box lid and place it on the box
# def box_close(robot):
    # Steps:
    # 1. Put gripper above the box lid
    # 2. Grab the lid with the gripper
    # 3. Align the lid with the box
    # 4. Place the lid on the box
    # First, put the gripper roughly above the box lid, so we don't bump it while trying to grab it.
    if check("the robot's gripper is not above the box lid"):
        robot.place("gripper above the box lid")
    # If the gripper isn't around the lid, put it around the lid.
    if check("the robot's gripper is not around the box lid and the robot's gripper is open"):
        robot.drop("gripper around the box lid")
    # If the gripper is near the lid and open, maybe we can grab it by closing the gripper.
    if check("the robot's gripper is near the box lid and the robot's gripper is open"):
        robot.close("gripper around the box lid")  
    # We closed the gripper, and the lid is still near the gripper, so maybe we grabbed it.
    # Try to move the lid to the box.
    if check("the robot's gripper is above the box lid and the robot's gripper is closed"):
        robot.place("lid on top of the box and let go")