
    # Steps:
    #  1. Put gripper near box lid
    #  2. Pick up box lid
    #  3. Place box lid on box
    # First, put the gripper near the box lid.
    if check("the robot's gripper is not near the box lid and the robot's gripper is not above the box lid"):
        robot.put("gripper near box lid")
    # Once the gripper is near the box lid, grab it.
    if check("the robot's gripper is near box lid and the robot's gripper is open"):
        robot.grab("box lid")
    # Once the gripper is around the box lid, try and place it on the box.
    if check("the robot's gripper is around the box lid and the box is not closed"):
        robot.put("box lid on box")